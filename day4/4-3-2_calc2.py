# TensorFlow 읽어 들이기 --- (※1)
import tensorflow as tf
with tf.compat.v1.Session() as sess:  
# 상수 정의하기 --- (※2)
    a = tf.constant(2)
    b = tf.constant(3)
    c = tf.constant(4)
    # 연산 정의하기 --- (※3)
    calc1_op = a + b * c
    calc2_op = (a + b) * c
    # 세션 시작하기 --- (※4)
    res1 = sess.run(calc1_op) # 식 평가하기
    print(res1)
    res2 = sess.run(calc2_op) # 식 평가하기
    print(res2)

