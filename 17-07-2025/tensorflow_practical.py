import tensorflow as tf
hello = tf.constant("hello world")
print(hello)
print(hello.numpy())
print(hello.numpy().decode("utf-8"))

a = tf.constant(10)
b = tf.constant(20)
c = a * b
print(c.numpy())

def input():
    return tf.constant([1,2,3])
def add(x,y):
    return x + y
x = input()
y = [1,2,3]
print("sum is",add(x,y).numpy())

li = tf.constant([1,2,3,4])
print("rank",tf.rank(li))
print("shape",tf.shape(li))
print("shape",tf.shape(li))






