import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped


class BumperbotTrajectory(Node):
    def __init__(self):
        super().__init__("bumperbot_trajectory")

        self.odom_sub_ = self.create_subscription(Odometry, "/bumperbot_controller/odom",self.odomCallback, 10)
        self.path_pub_ = self.create_publisher(Path, "/bumperbot_controller/trajectory",10)

        self.path_msg_ = Path()
        
        

    def odomCallback(self, msg):
        self.path_msg_.header.frame_id = msg.header.frame_id
        pose_stamped = PoseStamped()

        pose_stamped.header.frame_id = msg.header.frame_id
        pose_stamped.header.stamp = msg.header.stamp
        pose_stamped.pose = msg.pose.pose

        self.path_msg_.poses.append(pose_stamped)
        self.path_pub_.publish(self.path_msg_)
        
        



def main():
    rclpy.init()
    bumperbot_trajectory = BumperbotTrajectory()
    rclpy.spin(bumperbot_trajectory)
    bumperbot_trajectory.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()