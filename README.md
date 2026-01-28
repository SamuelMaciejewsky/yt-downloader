
# Overview

This script is designed to use the **pytubfix** tool to download YouTube videos on Windows. The goal is to create a script tailored to my preferences, focusing solely on downloading the video in the best available quality, and only the audio.

Currently, the script is configured to download audio in **M4A** format (though it's specified as MP3 in the code, which will be updated to MP3 in the future).

The code was developed to run on Python version **3.14.2**. Any other version may not be compatible, and the functionality is not guaranteed.

---

# Virtual Environment

I recommend using a virtual environment to avoid version incompatibilities and other potential issues with libraries in the code.

The Python version used is **3.14.2**, and the required libraries are listed in the **requirements.txt** file.

## Steps to Set Up the Virtual Environment

#### Step 1: Create the Virtual Environment
In this example, we'll create the virtual environment inside the cloned project folder. It's important to note that the name of the virtual environment does not necessarily need to be `.venv`. You can choose a different name if you'd like.

To create the environment, run the following command:

```
python -m venv .venv
```

#### Step 2: Activate the Virtual Environment
Once the environment is created, you need to activate it.

- If you're using **PowerShell** as a **Shell** (which I recommend as it’s what I used), run:

  ```
  .\.venv\Scripts\Activate.ps1
  ```

- If you're using **another shell**, try:

  ```
  .\.venv\Scriptsctivate #or .bat, .fish
  ```

- To exit the venv use the command:
 
  ```
  deactivate
  ```

#### Step 3: Install Dependencies
After activating the virtual environment, you can install the required dependencies.

Run the following command to install the dependencies from the **requirements.txt** file:

```
pip install -r requirements.txt
```

If this doesn’t work, try running:

```
python -m pip install -r requirements.txt
```

---


# How to Run

There are 2 ways to run the code:

1. **Without providing the link in the terminal**: In this case, you need to manually change the `video_url` variable in the code with the video link.

   Run the following command:

   ```
   python yt-download
   ```

   **To download in MP3 format**: If you prefer to download the audio in MP3 format, use the command:

   ```
   python yt-download mp3
   ```

2. **Using the link directly in the terminal**: You can pass the link directly in the command. The link must be enclosed in quotes.

   Run the following command:

   ```
   python yt-download manual "<link>"
   ```
   **To download the audio in MP3 format using the link**: To download the audio in MP3 format directly with the link, run:

   ```
   python yt-download manual "<link>" mp3
   ```

## Download Directory

The script uses the default video directory of the user to save the download. If you want to use a different directory, modify the `directory` variable with the path to your preferred directory.

---

# How to Modify the Code

If you want to modify the code, pay attention to the following points regarding the download directory management.

## Download Directory Management

The function responsible for retrieving the default Windows videos folder is `get_videos_folder()`:

```python
def get_videos_folder():
    # Access the Videos folder using the Windows API
    videos_folder = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Videos, 0, None)
    return videos_folder
```

It uses the `SHGetKnownFolderPath()` function from pywin32 lib to find the default video directory of the user on Windows. If you want to use a specific Windows directory or change the user directory, you can modify this function.

The variable `directory` is responsible for storing the final download directory path. It receives the value returned by the `get_videos_folder()` function and adds a subdirectory (in this case, `yt-downloader`):

```python
directory = get_videos_folder() + "\yt-downloader"
```

If you want to change the name of the subdirectory inside the "Videos" folder, simply replace `\yt-downloader` with your desired name.

The code below checks if the directory already exists. If it does not exist, it will be created. We recommend **not removing** this part of the code, as it ensures that the necessary directory is created if it doesn't already exist:

```python
if not os.path.exists(directory):
    os.makedirs(directory)
```

This check is important to ensure the download directory is available, preventing errors during the download process.

## Match Structure

The `match` structure is responsible for analyzing the number of arguments passed and applying the appropriate mode in the code. It ensures which mode will be used and stores the video URL if it is provided via command line.

### Detailed Breakdown of the `match` Structure

1. **Case 1**: This case checks if the code should run in the default mode, without command line parameters. No changes are needed in this case, as it already fulfills its purpose.

2. **Case 2**: This case has been modified to accept only 1 argument, which is the audio format, such as `mp3`. The code is simplified to handle only this parameter and download the audio:

3. **Case 3 and 4**: Cases 3 and 4 have been modified to handle arguments as `manual + link` and `manual + link + mp3`. If the `manual` mode is used, there must be at least 2 arguments: the `manual` mode and the video link. If `manual` mode is followed by the `mp3` argument, the code will download the audio.

## Downloading

### Creating the `YouTube` Object with the URL

After the `match` structure, the video URL is passed to the `pytubefix` library to create a `YouTube` object, which will manage the download process:

```python
yt = YouTube(video_url)
```

### Handling Issues with the URL

It is important to ensure that the provided link is valid. If there are any issues, the code should identify and handle them before attempting the download.

### Selecting Audio or Video

Next, the code checks whether the file being downloaded is a video or audio, based on the provided arguments. If it's a video, the code will download the highest resolution available:

```python
if audio_flag:
    # If audio
    stream = yt.streams.filter(only_audio=True).first()
else:
    # If video
    stream = yt.streams.get_highest_resolution()
```

### Download to the Specified Directory

Finally, the code downloads the video or audio to the desired directory, which was previously configured:

```python
stream.download(directory)
```

---

# Feedback and Contributions

I am not a Python programmer by profession, but I chose Python for its simplicity and the ease of finding useful libraries. Any feedback, suggestions, or ideas are very welcome! If you have any improvements, optimizations, or recommendations to make the code better, feel free to share.

Your contributions are greatly appreciated!
