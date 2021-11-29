import moviepy.editor as mp
messages = ["Dog", "Cat", "Duck", "Wolf"]
clips = [ mp.TextClip(txt, fontsize=170, color='green').set_duration(1)
          for txt in messages ]
concat_clip = mp.concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("texts.mp4")

from configurations.logger import MyLogger
logger = MyLogger().get_logger()


class Concatenation:

def encode_individual_video(alias: str, encode_details: EncodeVideoModel):
    """
    This API is used to create the new encoded pickle file of the
    new video details.
    ...
    Author
    --------------
    Name: Sahil Shah
    Company: Softvan
    ...

    Attributes
    ----------
    encode_details : dict
        Contains the data of project id and video id.

    Returns
    -------
    response : dict
        Contains the response of individual video encoding.
    """
    logger.info("encode_details: {} and alias: {} in {}".format(
        encode_details, alias, "encode_individual_video"))

    knit_project_id = encode_details.knit_project_id
    knit_video_id = encode_details.knit_video_id

    # if knit_project_id and knit_video_id:
    #     EncodeService.encode_individual_video_service(knit_project_id, alias,
    #                                           knit_video_id)
    #     response = AppServices.app_response(200,
    #                                         "successfully encoded the "
    #                                         "individual video")
    # else:
    #     response = AppServices.app_response(500, "knit_project_id or "
    #                                              "knit_video_id is missing")

    # logger.info("response: {} in {}".format(response,
    #                                         "encode_individual_video"))
    # return response


