# Audio Memory IO
The project is designed to simplify the transmission of audio in web services by using memory as the storage medium for audio, avoiding read and write operations on the hard drive, thus reducing service latency and the costs associated with hard drive maintenance and management.

## usage
install this repo by `pip install git+https://github.com/binsu996/audio_memory_io`, then you can read (using librosa) or write audio (using soundfile) normally, like this
```python
import audio_memory_io as amio
filename = "you_local_disk_audio_file.wav"

# load
y, sr = amio.load(filename, **other_librosa_kwargs)

#save 
r = amio.save(y, sr, "save_path.wav", **other_soundfile_kwargs)
assert r is None

# you can use None (default) as save path like below, the return value will be the audio file bytes
data_bytes = amio.save(y, sr, None, **other_soundfile_kwargs)


# the data_bytes object can be read by load method
y, sr = amio.load(data_bytes, **other_librosa_kwargs)

# when reviced an audio bytes from web app by a request like: curl -X POST -d @yourfile.wav http://example.com/upload
# let we assume that your the request obj you reviced is named req
# you can just load audio like this
y, sr = amio.load(req.body(), **other_librosa_kwargs)
```


