import tensorflow as tf
tf.compat.v1.disable_eager_execution()
# 데이터 플로우 그래프 구축하기 --- (※1)
a = tf.compat.v1.constant(20, name="a")
b = tf.compat.v1.constant(30, name="b")
mul_op = a * b

# 세션 생성하기 --- (※2)
with tf.compat.v1.Session() as sess : 

# TensorBoard 사용하기 --- (※3)
    tw = tf.compat.v1.summary.FileWriter("./day4/log_dir", graph=sess.graph)

# 세션 실행하기 --- (※4)
    print(sess.run(mul_op))
