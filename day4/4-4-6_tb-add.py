import tensorflow as tf
tf.compat.v1.disable_eager_execution()
# 상수와 변수 선언하기 --- (※1)
a = tf.compat.v1.constant(100, name="a")
b = tf.compat.v1.constant(200, name="b")
c = tf.compat.v1.constant(300, name="c")
v = tf.compat.v1.Variable(0, name="v")
# 곱셈을 수행하는 그래프 정의하기 --- (※2)
calc_op = a + b * c
assign_op = tf.compat.v1.assign(v, calc_op)
# 세션 생성하기 --- (※3)
with tf.compat.v1.Session() as sess:
    # TensorBoard 사용하기 --- (※4)
    tw = tf.compat.v1.summary.FileWriter("./day4/log_dir", graph=sess.graph)
# 세션 실행하기  --- (※5)
    sess.run(assign_op)
    print(sess.run(v))
