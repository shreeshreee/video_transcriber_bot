import re
import json
import os 

DATA_PATH = "../Data/transcripts/"

def extract_transcript(video_id : str, title : str):
    # Read the input file
    with open(DATA_PATH + video_id + "<>" + title + ".txt", "r") as file:
        content = file.read()
    # Extract the title using regex


    # Extract the text fields using regex
    text_matches = re.findall(r'"text": "(.*?)"', content)
    text = " ".join(text_matches)

    # Create a dictionary with the extracted data
    data = {
        "title": title,
        "text": text
    }

    return data

def append_to_jsonl(data, path):
    # Append the data to the jsonl file
    with open(path, "a") as file:
        json.dump(data, file)
        file.write("\n")

def main():
    # List the files in the directory
    files = os.listdir(DATA_PATH)

    # Extract the video ids and titles
    video_ids = [file.split("<>")[0] for file in files]
    titles = [file.split("<>")[1].replace(".txt", "") for file in files]



    # # Extract the transcript for each video
    for video_id, title in zip(video_ids, titles):
        print(f"Extracting transcript for video {video_id} with title {title}")
        data = extract_transcript(video_id.strip(), title.strip())
        append_to_jsonl(data, DATA_PATH + "transcripts.jsonl")

if __name__ == "__main__":
    main()