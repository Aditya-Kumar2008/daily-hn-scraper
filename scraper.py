import requests
import json
import datetime
import os

HN_URL = "https://hacker-news.firebaseio.com/v0"

def fetch_top_stories(limit=10):
    resp = requests.get(f"{HN_URL}/topstories.json")
    if resp.status_code != 200:
        return []
    
    story_ids = resp.json()[:limit]
    stories = []
    
    for sid in story_ids:
        s_resp = requests.get(f"{HN_URL}/item/{sid}.json")
        if s_resp.status_code == 200:
            data = s_resp.json()
            if data and data.get("type") == "story":
                stories.append(data)
                
    return stories

def generate_markdown(stories):
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    md = f"# Hacker News Daily Digest\n\n**Generated on:** {today}\n\n"
    
    for i, s in enumerate(stories, 1):
        title = s.get("title", "No Title")
        url = s.get("url", f"https://news.ycombinator.com/item?id={s.get('id')}")
        score = s.get("score", 0)
        by = s.get("by", "unknown")
        
        md += f"### {i}. [{title}]({url})\n"
        md += f"**Score:** {score} | **By:** {by} | [Comments](https://news.ycombinator.com/item?id={s.get('id')})\n\n"
        
    return md

if __name__ == "__main__":
    stories = fetch_top_stories()
    markdown_content = generate_markdown(stories)
    
    with open("DAILY_DIGEST.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("Successfully generated DAILY_DIGEST.md")
