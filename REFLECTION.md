# Reflection

## 1. What I'd Do Differently

If I were to start this project again, I would spend more time planning the project structure before implementing features. Moving common logic into utility functions earlier would have made testing and code maintenance easier. I would also add unit tests alongside each new feature instead of writing them at the end.

## 2. What's Still Unclear

I have a good understanding of the overall pipeline, but I would like to explore ByteTrack in greater depth. I understand its high-level concept of using both high-confidence and low-confidence detections for tracking, but I would like to learn more about how the association algorithm works internally and how it handles identity switches in challenging scenarios.

## 3. One ByteTrack Idea I'd Want to Try

I would like to integrate ByteTrack into this project so that detected people can be assigned persistent IDs across video frames. This would allow the application to track individuals over time instead of treating every frame independently. I would also like to compare the tracking performance using metrics such as MOTA and IDF1.