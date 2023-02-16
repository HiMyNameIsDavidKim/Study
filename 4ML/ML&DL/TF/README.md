# TensorFlow

### [DL 도구 활용]
* 손실 곡선
    * 훈련 과정에 발생된 지표 저장.
    * history = model.fit()
    * 손실함수(loss)와 정확도(accuracy)가 저장됨.
    * plt를 통해 플랏.
* 검증 손실 곡선
    * fit 메서드의 validation_data 매개변수에 검증데이터 입력.
    * history에 val_loss와 val_accuracy가 추가됨.
    * plt를 통해 플랏.
* 드롭 아웃
    * 훈련 과정에서 일부 뉴런을 랜덤하게 꺼서 과대적합 제어.
    * keras.layers.Dropout(0.X) 레이어 추가.
* 콜백
    * 과대적합이 시작되면 조기종료 후 최적 모델을 저장.
    * checkpoint = keras.callbacks.ModelCheckpoint() 클래스
    * early_stopping = keras.callbacks.EarlyStopping() 클래스
    * fit 메서드에 아래 파라미터 추가.
    * callbacks = [checkpoint, early_stopping]
<br><br>