# Samsung Internet Bookmark Converter

Converts bookmarks exported by the share functionality of Samsung Internet into the Netscape Bookmark File Format.

## Motivation

As of now, the [https://browser.samsung.com/beta](Samsung Internet Browser) does not support exporting bookmarks to the [https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582(v=vs.85)](Netscape Bookmark File Format) on android. Therefore, copying bookmarks to other browsers like [https://www.google.com/chrome/](Google Chrome) or [https://brave.com/](Brave) is pretty painful if you have a lot of bookmarks. Although Samsung Internet provides at least a way to export multiple bookmarks at once, but the format is not compatible with other browsers.

## Usage

## Step 1: Export bookmarks

Inside Samsung Internet, open the bookmarks. Select all bookmarks that you want to export. After that, click the share button and export it to your clipboard. Then, copy the bookmarks to a text file. The file should look something like this:

```text
GitHub
https://github.com/
YouTube
https://www.youtube.com/
DuckDuckGo
https://duckduckgo.com/
```

> [!NOTE]
> Under certain circumstances, the share function cannot be used for all bookmarks at once because too many bookmarks have been selected. In this case, the list of bookmarks to be exported must be divided into several chunks and copied into the same file.

## Step 2: Move the file to your desktop PC

This can be done by using [https://localsend.org/](LocalSend).

## Step 3: Run the script

From the terminal, run the script as follows:

```bash
python main.py <input_file> <output_file>
```

The output file will be an HTML file.

## Step 4: Move the output file to your mobile device

See step 2.

## Step 5: Import the bookmarks to the new browser

- Google Chrome: https://support.google.com/chrome/answer/96816?hl=en
- Brave: https://support.brave.app/hc/en-us/articles/360019782291-How-do-I-import-or-export-browsing-data#h_01K9ZM68CT1CTE2STFKMEDAG10