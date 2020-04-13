import tensorflow as tf
# 상수 정의하기 --- (※1)
a = tf.compat.v1.constant(120, name="a")
b = tf.compat.v1.constant(130, name="b")
c = tf.compat.v1.constant(140, name="c")
# 변수 정의하기 --- (※2)
v = tf.compat.v1.Variable(0, name="v")
# 데이터 플로우 그래프 정의하기 --- (※3)
calc_op = a + b + c
assign_op = tf.compat.v1.assign(v, calc_op)
# 세션 실행하기 --- (※4)
with tf.compat.v1.Session() as sess:
    sess.run(assign_op)
# v의 내용 출력하기 --- (※5)
    print(sess.run(v))
