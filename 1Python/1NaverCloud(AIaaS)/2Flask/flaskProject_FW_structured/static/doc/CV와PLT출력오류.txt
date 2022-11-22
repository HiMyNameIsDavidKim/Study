openCV는  BGR  사용 -> Red layer 가장 위로 -> 붉게 보임
	cv.imshow('Original', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

matplot는  RGB 사용 -> Blue layer 가장 위로 -> 푸르게 보임
	plt.imshow((lambda x: Image.fromarray(x))(img))
	plt.show()

# Blue Green Red