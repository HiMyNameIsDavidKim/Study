from sklearn.ensemble import RandomForestClassifier

def excute():
    clf = RandomForestClassifier(random_state=0)
    X = [[1,2,3],[11,12,13]] # 샘플 2개, 피쳐 3개
    y = [0,1] # 각 샘플의 클래스(타깃변수의 클래스값)
    clf.fit(X, y) # clf 객체를 통해 학습
    print(clf.predict([[4,5,6],[14,15,16]])) # 새로운 데이터셋의 클래스를 예측

if __name__ == '__main__':
    pass