import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Pong(Node):

    def __init__(self):
        super().__init__("Pong")
        self.publisher = self.create_publisher(String, 'pongping', 10)
        self.subscription = self.create_subscription(
            String,
            'pingpong',
            self.ping_callback,
            10)

    def ping_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        msg = String()
        msg.data = 'Pong' 
        self.publisher_.publish(msg)
        

def main(args=None):
        rclpy.init(args=args)
        node = Pong()
        rclpy.spin(node)
        rclpy.shutdown()


if __name__ == '__main__':
    main()
