# Prompt with one-sentence caption hit from the caption model of Panda-70M (https://github.com/snap-research/Panda-70M/tree/main/captioning)
# You can use this prompt to put the one-sentence caption hit into the prompt: defalut_prompt.format(${One-Sentence Caption}).

default_prompt = u"A wide image is given containing a 2x4 grid of 8 equally spaced video frames. They're arranged chronologically from left to right, and then from top to down, all separated by white borders. This video depicts \"{}\". Please imagine the video based on the sequence of 8 frames, and provide a faithfully concise description of the following content:\n" \
"1. Detailed description of this video in more than three sentences. Here are some examples of good descriptions: 1) A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse. She wears sunglasses and red lipstick. She walks confidently and casually. The street is damp and reflective, creating a mirror effect of the colorful lights. Many pedestrians walk about. 2) A movie trailer featuring the adventures of the 30 year old space man wearing a red wool knitted motorcycle helmet, blue sky, salt desert, cinematic style, shot on 35mm film, vivid colors.\n" \
"2. Description of the main subject actions or status sequence. This suggests including the main subjects (person, object, animal, or none) and their attributes, their action, their position, and movements during the video frames.\n" \
"3. Summary of the background. This should also include the objects, location, weather, and time.\n" \
"4. Summary of the view shot, camera movement and changes in shooting angles in the sequence of video frames.\n" \
"5. Briefly one-sentence Summary of the visual, Photographic and artistic style.\n" \
"No need to provide summary content. Do not describe each frame individually. Do not reply with words like 'first frame'. The description should be useful for AI to re-generate the video."

# We also provide another prompt that doesn't require running any other caption models. We tested it on a small number of samples, and the results were almost the same.
default_prompt_wo_hit = u"A wide image is given containing a 2x4 grid of 8 equally spaced video frames. They're arranged chronologically from left to right, and then from top to down, all separated by white borders. Please imagine the video based on the sequence of 8 frames, and provide a faithfully concise description of the following content:\n" \
"1. Detailed description of this video in more than three sentences. Here are some examples of good descriptions: 1) A stylish woman walks down a Tokyo street filled with warm glowing neon and animated city signage. She wears a black leather jacket, a long red dress, and black boots, and carries a black purse. She wears sunglasses and red lipstick. She walks confidently and casually. The street is damp and reflective, creating a mirror effect of the colorful lights. Many pedestrians walk about. 2) A movie trailer featuring the adventures of the 30 year old space man wearing a red wool knitted motorcycle helmet, blue sky, salt desert, cinematic style, shot on 35mm film, vivid colors.\n" \
"2. Description of the main subject actions or status sequence. This suggests including the main subjects (person, object, animal, or none) and their attributes, their action, their position, and movements during the video frames.\n" \
"3. Summary of the background. This should also include the objects, location, weather, and time.\n" \
"4. Summary of the view shot, camera movement and changes in shooting angles in the sequence of video frames.\n" \
"5. Briefly one-sentence Summary of the visual, Photographic and artistic style.\n" \
"No need to provide summary content. Do not describe each frame individually. Do not reply with words like 'first frame'. The description should be useful for AI to re-generate the video."