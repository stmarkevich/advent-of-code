
video:
	rm -f map_*.png
	rm -f video.mp4
	python visualization.py
	ffmpeg -i map_%06d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p video.mp4

clean:
	rm -vf map_*.png
	rm -vf video.mp4