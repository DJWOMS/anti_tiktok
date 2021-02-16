import shutil
from uuid import uuid4
from fastapi import UploadFile, BackgroundTasks, HTTPException

from models import Video, User
from schemas import UploadVideo


async def save_video(
        user: User,
        file: UploadFile,
        title: str,
        description: str,
        back_tasks: BackgroundTasks
):
    file_name = f'media/{user.id}_{uuid4()}.mp4'
    if file.content_type == 'video/mp4':
        back_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't mp4")
    info = UploadVideo(title=title, description=description)
    return await Video.objects.create(file=file_name, user=user, **info.dict())


def write_video(file_name: str, file: UploadFile):
    # async with aiofiles.open(file_name, "wb") as buffer:
    #     data = await file.read()
    #     await buffer.write(data)
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)































# def ranged(
#             file: IO[bytes],
#             start: int = 0,
#             end: int = None,
#             block_size: int = 8192,
#     ) -> Generator[bytes, None, None]:
#         consumed = 0
#
#         file.seek(start)
#         while True:
#             data_length = min(block_size, end - start - consumed) if end else block_size
#             if data_length <= 0:
#                 break
#             data = file.read(data_length)
#             if not data:
#                 break
#             consumed += data_length
#             yield data
#
#         if hasattr(file, 'close'):
#             file.close()



    # file = await Video.objects.select_related('user').get(pk=video_pk)
    # # file_like = open(file.dict().get('file'), mode="rb")
    # path = Path(file.dict().get('file'))
    # file = path.open('rb')
    # file_size = path.stat().st_size
    #
    # content_length = file_size
    # status_code = 200
    # headers = {}
    # content_range = request.headers.get('range')
    # if content_range is not None:
    #     content_range = content_range.strip().lower()
    #     content_ranges = content_range.split('=')[-1]
    #     range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
    #     range_start = max(0, int(range_start)) if range_start else 0
    #     range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
    #     content_length = (range_end - range_start) + 1
    #     file = ranged(file, start=range_start, end =range_end + 1)
    #     status_code = 206
    #     headers['Content-Range'] = f'bytes {range_start}-{range_end}/{file_size}'
    # response = StreamingResponse(
    #     file,
    #     media_type='video/mp4',
    #     status_code=status_code,
    # )
    # response.headers.update({
    #     'Accept-Ranges': 'bytes',
    #     'Content-Length': str(content_length),
    #     **headers,
    # })
    return response
