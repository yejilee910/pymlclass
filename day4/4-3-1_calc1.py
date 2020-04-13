# TensorFlow 추출하기 --- (※1)
import tensorflow as tf
with tf.compat.v1.Session() as sess:

    # 상수 정의 --- (※2)
    a = tf.compat.v1.constant(1234)
    b = tf.compat.v1.constant(5000)
# 계산 정의 --- (※3)
    add_op = a + b
# 세션 시작하기 --- (※4)
    # sess = tf.compat.v1.Session()
    res = sess.run(add_op)  # 식 평가하기
print(res)
