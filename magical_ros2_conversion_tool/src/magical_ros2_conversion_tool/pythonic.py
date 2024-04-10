PYTHON_REPLACEMENTS = {
    r'\n(\s+)rospy.init_node\((.*)\)': '\n$0rclpy.init(args=args)\n$0node = ClassName($1)\n$0rclpy.spin(node)\n$0rclpy.shutdown()',
    r'rospy.Publisher\(([^\,]+), ([^\)]+)\)': 'self.create_publisher($1, $0)',
    r'rospy.Subscriber\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_subscription($1, $0, $2)',
    r'rospy.Service\(([^\,]+), ([^\,]+), ([^\)]+)\)': 'self.create_service($1, $0, $2)',
    r'\n(\s+)([^\s]+)[\ \t]*=[\ \t]*rospy\.get_param\(([^\,\n]+),[\ \t]*([^\s]+)\)': '\n$0$1 = self.declare_parameter($2, $3)',
    r'\n(\s+)([^\s]+)[\ \t]*=[\ \t]*rospy\.get_param\(([^\,\n]+)\)': '\n$0$1 = self.declare_parameter($2, rclpy.Parameter.Type.DOUBLE)',
}


def update_python(package):
    package.source_code.modify_with_patterns(PYTHON_REPLACEMENTS, language='python')
