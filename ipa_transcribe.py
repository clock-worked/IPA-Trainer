import requests
import os
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://unalengua.com',
    'Referer': 'https://unalengua.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0',
    'sec-ch-ua': '"Opera GX";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def transcribe(text):
    json_data = {
    'text': text,
    'lang': 'en-US',
    'mode': True,
    }

    response = requests.post('https://api2.unalengua.com/ipav3', headers=headers, json=json_data)

    save = response.json()
    ipa = save['ipa']
    
    return ipa

def main():
    text_file = open("words.txt", "r")
    
    # Read each line in the file and transcribe it
    for line in text_file:
        ipa = transcribe(line)
        # Write the IPA to a file
        with open("ipa.txt", "a", encoding="utf-8") as ipa_file:
            ipa_file.write(ipa)
            
            print("{} -> {}".format(line, ipa))
            

    
if __name__ == "__main__":
    main()

