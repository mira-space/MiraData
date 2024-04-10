<p align="center">
  <img src="assets/miralogo_s.png" height=80>
</p>

<div align="center">

## MiraData:  A Large-Scale Video Dataset with Long Durations and Structured Captions

> [Xuan Ju](https://github.com/juxuan27)<sup>1*</sup>, [Yiming Gao](https://scholar.google.com/citations?user=uRCc-McAAAAJ&hl=zh-TW)<sup>1*</sup>, [Zhaoyang Zhang](https://zzyfd.github.io/)<sup>1</sup>, [Ziyang Yuan]()<sup>1</sup>,  [Xintao Wang](https://xinntao.github.io/)<sup>1#</sup>,  [Ailing Zeng](), [Yu Xiong](), [Qiang Xu](),  [Ying Shan](https://www.linkedin.com/in/YingShanProfile/)<sup>1</sup>, <br>
> <sup>1</sup>ARC Lab, Tencent PCG <sup>*</sup>Equal contribution  <sup>#</sup>Project lead

<!-- [![arXiv](https://img.shields.io/badge/arXiv-2404.xxxxx-b31b1b.svg)](https://arxiv.org/abs/2404.xxxxx) -->
[![Project Page](https://img.shields.io/badge/Project-Website-green)](https://mira-space.github.io/)
</div>

## Introduction

Video datasets play a crucial role in video generation such as [sora](https://openai.com/sora).
However, existing text-video datasets often fall short when it comes to **handling long video sequences** and **capturing shot transitions**.
To address these limitations, we introduce **MiraData** (**Mi**ni-So**ra** Data), a large-scale video dataset designed specifically for long video generation tasks.

#### **Key Features of MiraData**

1. **Long Video Duration**: Unlike previous datasets, where video clips are often very short (typically less than 6 seconds), MiraData focuses on uncut video segments with durations ranging from 1 to 2 minutes. This extended duration allows for more comprehensive modeling of video content.
2. **Structured Captions**: Each video in MiraData is accompanied by structural captions. These captions provide detailed descriptions from various perspectives, enhancing the richness of the dataset. The average caption length is 349 words, ensuring a thorough representation of the video content.

#### Current Status

In this initial release, MiraData includes two scenarios:

- Gaming: Videos related to gaming experiences.
- City/Scenic Exploration: Videos capturing urban or scenic views.

MiraData is still in its early stages, and we will release more scenarios and improve the quality of the dataset in the near future.

<h3 align='center'>Demo Video</h3>

[![MiraData](https://i.ytimg.com/vi/3G0p7Jo3GYM/maxresdefault.jpg)](https://www.youtube.com/watch?v=3G0p7Jo3GYM "MiraData")


## Dataset

### Meta Files

[![MetaFile-ALL](https://img.shields.io/badge/MetaFile-All-green)](https://drive.google.com/file/d/18UGbtUFQSLG-0WT35AFukdGjnwej_1Pn/view?usp=sharing)
[![MetaFile-Samples](https://img.shields.io/badge/MetaFile-Samples-green)](https://github.com/mira-space/MiraData/blob/main/assets/miradata_v0_100_samples.csv)

This version of MiraData contains 57,803 video clips with an overall of 1,754 hours, containing two scenarios: gaming and city/scenic exploration. The clip number and video duration is shown as follows:

  | Scenario          | Clip Num | Video Duration |
  |-----------------|----------|-----------------|
  | Gaming | 31,159 | 893 hrs  |
  | City/Scenic Exploration  | 26,644 | 861 hrs |

The meta file for this version of MiraData is provided [here](https://drive.google.com/file/d/18UGbtUFQSLG-0WT35AFukdGjnwej_1Pn/view?usp=sharing). Additionally, for a better and quicker understanding of our meta file composition, we randomly sample a set of 100 video clips, which can be accessed [here](assets/miradata_v0_100_samples.csv). The meta file contains the following index information:

- **index**: video clip index, which is composed of `{download_idx}_{video_id}-{clip_id}`
- **video_id**: youtube video id
- **start_frame**: clip start frame of the youtube video
- **end_frame**: clip end frame of the youtube video
- **main_object_caption**: caption of the main object in video
- **background_caption**: caption of the video background
- **style_caption**: caption of the video style
- **camera_caption**: caption of the camera movie
- **short_caption**: a short overall caption
- **dense_caption**: a dense overall caption
- **fps**: the video fps used for extracting frame

*Note that you can obtain the start and end timestamps by using start_frame/fps or end_frame/fps.*

### How to Download

To download the videos and split the videos into clips, you can use the following scripts:

```
python download_data.py --meta_csv miradata_v0.csv --video_start_id 0 --video_end_id 10631 --raw_video_save_dir miradata/raw_video --clip_video_save_dir miradata/clip_video
```

where the `--video_start_id` and `--video_end_id` indicates the start and end values of the `download_idx` in meta file's `index` for downloading. The gaming scenario is ranging from 0 to 7416 and the city/scenic exploration is ranging from 7417 to 10631.

### Collection and Annotation

To collect the MiraData, we first manually select youtube channels in different scenarios. Then, all the videos in corresponding channels are downloaded and splitted using [PySceneDetect](https://www.scenedetect.com/). After that, we selected video clips with a duration ranging from 1 to 2 minutes. For video clips longer than 2 minutes, we split them into multiple 2-minute clips. Finally, we caption the video clip using GPT-4V.

#### Structured Captions

Each video in MiraData is accompanied by structured captions. These captions provide detailed descriptions from various perspectives, enhancing the richness of the dataset.

**Six Types of Captions**

- Main Object Description: Describes the primary object or subject in the video, including their attributes, actions, positions, and movements throughout the video.
- Background: Provides context about the environment or setting, including objects, location, weather, and time.
- Style: Covers artistic style, visual and photographic aspects, such as realistic, cyberpunk, and cinematic style.
- Camera Movement: Details any camera pans, zooms, or other movements.
- Short Caption: A concise summary capturing the essence of the video, generated using the [Panda-70M](https://github.com/snap-research/Panda-70M/tree/main/captioning) caption model.
- Dense Caption: A more elaborate and detailed description that summarizes the above five types of captions.

#### Captions with GPT-4V

We tested the existing open-source visual LLM methods and GPT-4V, and found that GPT-4V's captions show better accuracy and coherence in semantic understanding in terms of temporal sequence. It also provides more accurate descriptions of the main subject and background objects, with fewer object omissions and less hallucination issues. Therefore, we use GPT-4V to generate Dense Captions, Main Object Descriptions, Background Descriptions, Camera Movement Descriptions, and Video Styles.

In order to balance annotation costs and caption accuracy, we uniformly sample 8 frames for each video and arrange them into a 2x4 grid of one large image. Then, we use the caption model of [Panda-70M](https://github.com/snap-research/Panda-70M/tree/main/captioning) to annotate each video with a one-sentence caption, which serves as a hint for the main content, and input it into our fine-tuned prompt. By feeding the fine-tuned prompt and a 2x4 large image to GPT-4V, we can efficiently output captions for multiple dimensions in just one round of conversation. The specific prompt content can be found in the [caption_gpt4v.py](caption_gpt4v.py), and we welcome everyone to contribute to the more high-quality text-video data. :raised_hands:

## Statistic

<div style="display:inline-block" align=center>
     <img src="assets/statistic_dense.png" width="350"/>
    <img src="assets/statistic_full.png" width="350"/>
</div>

<div style="display:inline-block" align=center> &nbsp;&nbsp;&nbsp;&nbsp; Total text length statistics of dense captions. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Total text length statistics of six types of captions.</div>


<div style="display:inline-block" align=center>
     <img src="assets/wordcloud_short.png" width="300"/>
    <img src="assets/wordcloud_dense.png" width="300"/>
</div>

<div style="display:inline-block" align=center>Word cloud of short captions. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Word cloud of dense captions.</div>

## Demonstration

### Video-Caption Pairs in MiraData

  <table class="center">
    <tr>
      <td width=10% style="border: none"><p>Video</p></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/b2989b1f-d8d0-42d1-b337-2d1e6b6a0f11"></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/1cb6562b-b99c-4ba6-ab81-215771ea6657"></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/c388f3a4-ced7-4fc2-937b-49b482cb8390"></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Main Object Caption</p></td>
      <td width=30% style="border: none"><p>A futuristic car, is seen driving through various parts of the neon city. Initially, the car is at a standstill, showcasing its design and lighting, before accelerating into the traffic. The car maneuvers through the streets, dodging other vehicles and obstacles, with a change in perspective to a first-person view showing a hand holding a gun, suggesting a shift to an action sequence or a new gameplay mechanic. The car's movement is fluid and fast, indicating high-speed travel through the city.</p></td>
      <td width=30% style="border: none"><p>From the player's perspective, initially grapples with an adversary, as evidenced by the close-up of mechanical parts and the player's hands. The focus then shifts to the elderly woman, who is initially aggressive or defensive, holding a shovel raised as if ready to strike. She then turns, leading the player around the side of a wooden structure, possibly her house. Over time, her demeanor softens, and she appears to be talking to the player, as she lowers her shovel and adopts a more relaxed posture.</p></td>
      <td width=30% style="border: none"><p>A person, is seen walking at a leisurely pace along a path that cuts through the ancient ruins and natural landscape. They appear to be exploring the area, moving from the open spaces between the large arches into a more enclosed tunnel. Their movement is consistent and unhurried, suggesting a relaxed and contemplative stroll through the historic site.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Background Caption</p></td>
      <td width=30% style="border: none"><p>A bustling, rain-slicked metropolis at night, characterized by towering skyscrapers, bright neon signs, and holographic billboards. The weather is rainy, creating reflective surfaces on the roads that mirror the city's vivid lights. The time is night, which is evident from the artificial lighting and dark sky, contributing to the cyberpunk aesthetic of the environment.</p></td>
      <td width=30% style="border: none"><p>The background depicts a lush rural setting with a wooden house or shed, surrounded by greenery, rocks, and patches of red flowers. The environment has a naturalistic feel, with a clear sky and daylight indicating a daytime setting. There are no other characters or moving elements visible in the background, which suggests a peaceful, albeit isolated, location.</p></td>
      <td width=30% style="border: none"><p>A picturesque scene of an ancient city in ruins, with large brick arches and remnants of structures that speak to a bygone era. The setting is peaceful and natural, with trees, bushes, and grasses softly swaying in the light breeze. The time appears to be late afternoon or early evening, as indicated by the long shadows and the warm, soft light that bathes the scene, likely the golden hour before sunset.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Style Caption</p></td>
      <td width=30% style="border: none"><p>The visual, photographic, and artistic style is reminiscent of a cyberpunk universe, with a strong emphasis on neon lighting, rain-drenched streets, and a high-contrast color palette that creates a sense of depth and vibrancy.</p></td>
      <td width=30% style="border: none"><p>The visual style is realistic with detailed character models, natural lighting, and a high level of environmental detail, creating an immersive and believable rural setting in a video game context.</p></td>
      <td width=30% style="border: none"><p>The video exhibits a cinematic and picturesque quality, utilizing natural lighting and the historical setting to create a visually rich and contemplative narrative.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Camera Caption</p></td>
      <td width=30% style="border: none"><p>The view shot starts with a third-person perspective from behind the car, giving a clear view of the vehicle and its immediate surroundings. The camera then transitions to a first-person perspective, showing the driver's hand with a gun, implying a change in gameplay or narrative. The camera angles vary, capturing the high-speed motion of the car from different viewpoints, including a dynamic, forward-facing angle that conveys the sensation of speeding through the city.</p></td>
      <td width=30% style="border: none"><p>The camera perspective is consistent with a first-person viewpoint throughout the sequence. The initial frame suggests a dynamic struggle with rapid movement, while the subsequent frames show a steadier camera as the player interacts with the woman. The camera follows the woman as she moves, maintaining her as the focal point, and the shooting angles change as the player's perspective shifts to keep the woman in view, particularly as she moves and turns.</p></td>
      <td width=30% style="border: none"><p>The camera follows a steady, linear path, maintaining a consistent distance from the main subject. It captures the scene from a series of angles that alternate between showcasing the expansive ruins and focusing on the path ahead. As the person enters the tunnel, the camera angle shifts to frame them against the light at the end of the tunnel, creating a silhouette effect.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Short Caption</p></td>
      <td width=30% style="border: none"><p>The player is driving a futuristic car in a neon-lit city at night.</p></td>
      <td width=30% style="border: none"><p>A video game character standing in front of a house.</p></td>
      <td width=30% style="border: none"><p>There is a person walking on a path surrounded by trees and ruins of an ancient city.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Dense Caption</p></td>
      <td width=30% style="border: none"><p>A player navigating a sleek, futuristic car through a neon-lit cityscape at night. The city is alive with vibrant colors, illuminated advertisements, and dynamic lighting that reflects off the wet streets, adding to the sense of speed and movement. The car's design is cutting-edge, with glowing elements and a streamlined shape that suggests advanced technology and high performance. As the player drives, the environment whizzes by, creating a blur of lights and structures that enhances the feeling of racing through this urban playground.</p></td>
      <td width=30% style="border: none"><p>The video sequence showcases a first-person perspective of a video game character interacting with a non-playable character (NPC) in a rural environment. Initially, the player character appears to be grappling with an enemy or creature, as indicated by the close-up struggle and the presence of sparks or embers. The scene transitions to the player character standing before an elderly woman, who is wielding a shovel in a defensive or threatening posture. The woman's expressions and stance suggest she is wary or confrontational towards the player. As the video progresses, the woman seems to relax slightly, lowering her shovel and engaging in conversation with the player, indicated by her changing facial expressions and body language.</p></td>
      <td width=30% style="border: none"><p>A serene and historical ambiance as a person walks through a path surrounded by the lush greenery and the majestic ruins of an ancient city. The ruins feature large arches and weathered brick walls, hinting at a grand past. The path is well-trodden and flanked by trees and grass, with the golden hour sunlight casting a warm glow over the scene. Other visitors can be seen in the distance, enjoying the tranquil environment. As the person progresses, they pass through a tunnel-like structure, where the play of light and shadow creates a dramatic effect, enhancing the sense of exploration and discovery.</p></td>
    </tr>
  </table>



  <table class="center">
    <tr>
      <td width=10% style="border: none"><p>Video</p></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/aeaf4b11-1fae-4a80-9ff0-ea6d01fdc755"></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/b213cf2a-a04d-4d46-aa23-9dbaf8116ede"></td>
      <td width=30% style="border: none"><video src="https://github.com/mira-space/MiraData/assets/89566272/2adf3418-093d-48ec-86f6-81c8537596c5"></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Main Object Caption</p></td>
      <td width=30% style="border: none"><p>There are no main subjects such as people or animals that are the focus of the video. Instead, the video's main subject is the changing urban landscape itself. The sequence shows a transition from a pedestrian-friendly street with sidewalks to an area with construction barriers and finally to a riverside scene with the bridge as a focal point.</p></td>
      <td width=30% style="border: none"><p>A cyclist, is seen navigating through the city streets. Starting on a quieter street, the cyclist passes by shops with inviting warm lighting and continues through intersections and alongside parked cars. The rider's movement is fluid and uninterrupted, suggesting a familiarity with the route. The bicycle's lights are on, ensuring visibility as the evening darkens.</p></td>
      <td width=30% style="border: none"><p>Throughout the video, the main subjects are the pedestrians who are walking at a leisurely pace. They are scattered across the walkway, maintaining a casual flow of movement. Their attire suggests a warm and comfortable climate, and their relaxed demeanor indicates a peaceful setting. The fountain in the early part of the video adds a dynamic element as water sprays rhythmically, while the statue towards the end stands still, providing a contrast to the moving subjects.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Background Caption</p></td>
      <td width=30% style="border: none"><p>A cityscape that includes a mix of architectural styles, from red-brick buildings to industrial metal structures. The weather appears to be clear and sunny, with blue skies and minimal cloud cover. The time seems to be during the day, given the shadows and the brightness of the sunlight.</p></td>
      <td width=30% style="border: none"><p>A cityscape at twilight, with the sky dimming as the video progresses. The streets are moderately busy with pedestrians and occasional vehicles. The architecture is a mix of residential buildings, small businesses, and modern commercial spaces. Streetlights and building lights provide illumination, and the weather appears clear and calm.</p></td>
      <td width=30% style="border: none"><p>Features a blend of natural and urban elements. The plaza with the fountain is surrounded by buildings that suggest a downtown area, while the walkway is bordered by lush greenery, indicating well-kept urban parks or gardens. The clear blue sky suggests fair weather, and the bright sunlight indicates daytime, possibly morning or afternoon given the angle of the shadows.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Style Caption</p></td>
      <td width=30% style="border: none"><p>The visual, photographic, and artistic style of the video is realistic with a clear, bright, and high-contrast depiction of an urban environment during a sunny day.</p></td>
      <td width=30% style="border: none"><p>The visual style of the video is naturalistic and immersive, capturing the tranquil ambiance of a city transitioning from day to night with a steady, first-person perspective.</p></td>
      <td width=30% style="border: none"><p>The video showcases a wide-angle, high-definition view with vivid colors and a clear focus, capturing the tranquility and beauty of a city's public space in a documentary-style presentation.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Camera Caption</p></td>
      <td width=30% style="border: none"><p>The camera movement is smooth and appears to be a tracking shot moving forward through the city street. The shooting angle is mostly at street level, providing a first-person perspective of the environment. The camera angle shifts slightly upwards as the video progresses, especially as the bridge becomes the central element in the later frames.</p></td>
      <td width=30% style="border: none"><p>The camera angle is consistent throughout the video, maintaining a first-person perspective that likely mimics the cyclist's point of view. The camera moves smoothly, following the natural motion of cycling, and there are no abrupt changes in direction or speed. This steady camera work allows for an immersive experience as if the viewer is the one riding the bicycle.</p></td>
      <td width=30% style="border: none"><p>The camera appears to move smoothly along the walkway, maintaining a consistent level and distance from the ground, providing a continuous perspective of the environment. The angle of the shots changes as the camera progresses, starting with a frontal view of the fountain and transitioning to a path leading towards the statue, suggesting a linear path of travel.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Short Caption</p></td>
      <td width=30% style="border: none"><p>A view of a city street with a bridge in the background.</p></td>
      <td width=30% style="border: none"><p>A person is riding a bicycle on a city street at night, passing by various buildings and cars.</p></td>
      <td width=30% style="border: none"><p>People are walking on a sidewalk in a city, and there is a fountain in the middle of the street.</p></td>
    </tr>
    <tr style="text-align: center;">
      <td width=10% style="border: none"><p>Dense Caption</p></td>
      <td width=30% style="border: none"><p>The video presents a panoramic journey through a city street leading towards a bridge. The sequence begins with a view of a well-maintained urban area, featuring red-brick buildings with large windows and street lamps, and transitions towards a more industrial setting with metal structures and a bridge in the background. The progression of the frames suggests a movement from a commercial zone towards a waterfront area, with the bridge becoming increasingly prominent in the view.</p></td>
      <td width=30% style="border: none"><p>The essence of a city at dusk, with the sky transitioning from the last hints of daylight to the onset of night. A person rides a bicycle along the city streets, weaving through the urban landscape that is a mix of residential and commercial areas. The streets are lined with a variety of buildings, from cozy eateries to modern storefronts, all under the soft glow of streetlights and the occasional bright signage. The cyclist moves at a steady pace, allowing viewers to take in the serene atmosphere of the city in the evening.</p></td>
      <td width=30% style="border: none"><p>A serene urban scene where people are leisurely walking along a wide sidewalk in a city. The initial frames show a modern plaza with a reflective surface, where water jets from a fountain create a playful and refreshing atmosphere. As the video progresses, the perspective shifts away from the fountain plaza to a tree-lined walkway, with well-maintained grassy areas on either side. Pedestrians of various ages can be seen strolling, some alone and others in groups, indicating a relaxed urban environment. The latter part of the video reveals a statue prominently positioned at the end of the walkway, adding a historical or cultural dimension to the cityscape.</p></td>
    </tr>
  </table>

  

<sup>**We will remove the video samples from our dataset / Github / project webpage as long as you need it. Please [contact to us](#Contact-Information) for the request.</sup>

## License Agreement

Please see [LICENSE](./LICENSE).

- The MiraData dataset is only available for informational purposes only. The copyright remains with the original owners of the video.
- All videos of the MiraData dataset are obtained from the Internet which are not property of our institutions. Our institution are not responsible for the content nor the meaning of these videos.
- You agree not to reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purposes, any portion of the videos and any portion of derived data. You agree not to further copy, publish or distribute any portion of the MiraData dataset.

## Citation

If you find this project useful for your research, please cite our paper. :blush:

## Acknowlegement

This README file is adpated from [Panda-70M](https://github.com/snap-research/Panda-70M/blob/main/README.md)

## Contact Information

For any inquiries, please email `mira-x@googlegroups.com`.
