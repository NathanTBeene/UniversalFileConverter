conversions = {
    'AVI': ['MP4', 'MKV', 'MOV', 'WMV', 'FLV', 'MP3'],
    'MP4': ['AVI', 'MKV', 'MOV', 'MPEG', 'GIF', 'MP3'],
    'MOV': ['MP4', 'AVI', 'MKV', 'FLV', 'MP3'],
    'MKV': ['MP4', 'AVI', 'MOV', 'WMV', 'MP3'],
    'WMV': ['MP4', 'AVI', 'MOV', 'MKV', 'MP3'],
    'FLV': ['MP4', 'AVI', 'MOV', 'MKV', 'MP3'],
    'MP3': ['WAV', 'AAC', 'OGG', 'FLAC'],
    'WAV': ['MP3', 'AAC', 'OGG', 'FLAC'],
    'AAC': ['MP3', 'WAV', 'OGG', 'FLAC'],
    'OGG': ['MP3', 'WAV', 'AAC', 'FLAC'],
    'FLAC': ['MP3', 'WAV', 'AAC', 'OGG'],
    'WEBM': ['MP4', 'AVI', 'MKV'],
    'MPEG': ['MP4', 'AVI', 'MKV', 'MOV'],
    'GIF': ['MP4', 'AVI', 'MOV'],
    "PNG": ["JPG", "JPEG", "GIF", "BMP", "WEBP", "TIFF"],
    "JPG": ["PNG", "GIF", "BMP", "WEBP", "TIFF"],
    "JPEG": ["PNG", "GIF", "BMP", "WEBP", "TIFF"],
    "GIF": ["PNG", "JPG", "JPEG", "BMP", "WEBP", "TIFF"],
    "BMP": ["PNG", "JPG", "JPEG", "GIF", "WEBP", "TIFF"],
    "WEBP": ["PNG", "JPG", "JPEG", "GIF", "BMP", "TIFF"],
    "TIFF": ["PNG", "JPG", "JPEG", "GIF", "BMP", "WEBP"]
    
}

file_formats = list(conversions)