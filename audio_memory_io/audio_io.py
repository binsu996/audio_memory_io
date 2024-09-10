import soundfile as sf
import io
import librosa
import pathlib as Path


def load_bytes(bytes_data, **librosa_kwargs):
    audio_in_memory = io.BytesIO(bytes_data)
    return librosa.load(audio_in_memory, **librosa_kwargs)


def load(filename_or_bytes, **librosa_kwargs):
    if Path(filename_or_bytes).exists():
        return librosa.load(filename_or_bytes, **librosa_kwargs)
    else:
        try:
            return load_bytes(filename_or_bytes, **librosa_kwargs)
        except:
            raise RuntimeError(
                "filename_or_bytes is neither an existing path nor a bytes object")


def save(y, sr, filename=None, **soundfile_kwargs):

    if len(y.shape) == 2:
        y = y.T

    if filename is None:
        format = soundfile_kwargs.pop("format", "WAV")
        buffer = io.BytesIO()
        sf.write(buffer, y, 24000, format=format, **soundfile_kwargs)
        buffer.seek(0)
        binary_data = buffer.getvalue()
        return binary_data
    else:
        sf.write(filename, y, sr, **soundfile_kwargs)
        return None
