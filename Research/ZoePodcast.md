# Fine tuning an LLM on Zoe Podcast Transcripts 

## Data Gathering and Preparation 

### Video Transcripts 

#### Podcast links: 

Podcast playlist at:
 https://www.youtube.com/playlist?list=PLArLFV5giiuJLGM56icM90tz42kIC7jfB 

    const videoTitles = document.querySelectorAll('a[id="video-title"]');
    const hrefList = Array.from(videoTitles).map(title => title.getAttribute('href'));

Data stored in **zoe_podcast_links.json**

### Podcast transcripts using