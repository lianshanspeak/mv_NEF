import os
import shutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

class NEFCopierApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('NEF 文件拷贝工具')

        self.source_folder = ''
        self.target_folder = ''

        self.source_button = QtWidgets.QPushButton('选择源文件夹', self)
        self.source_button.clicked.connect(self.select_source_folder)

        self.target_button = QtWidgets.QPushButton('选择目标文件夹', self)
        self.target_button.clicked.connect(self.select_target_folder)

        self.copy_button = QtWidgets.QPushButton('开始拷贝', self)
        self.copy_button.clicked.connect(self.copy_nef_to_target)

        self.source_label = QtWidgets.QLabel('源文件夹: 未选择', self)
        self.target_label = QtWidgets.QLabel('目标文件夹: 未选择', self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.source_button)
        layout.addWidget(self.source_label)
        layout.addWidget(self.target_button)
        layout.addWidget(self.target_label)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)
        self.resize(300, 200)

    def select_source_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(self, "选择源文件夹")
        if self.source_folder:
            self.source_label.setText(f"源文件夹: {self.source_folder}")

    def select_target_folder(self):
        self.target_folder = QFileDialog.getExistingDirectory(self, "选择目标文件夹")
        if self.target_folder:
            self.target_label.setText(f"目标文件夹: {self.target_folder}")

    def copy_nef_to_target(self):
        if not self.source_folder or not self.target_folder:
            QMessageBox.warning(self, "警告", "请先选择源文件夹和目标文件夹")
            return

        jpg_files = [f for f in os.listdir(self.target_folder) if f.lower().endswith('.jpg')]
        for jpg_file in jpg_files:
            nef_file = jpg_file.rsplit('.', 1)[0] + '.NEF'
            source_file = os.path.join(self.source_folder, nef_file)
            target_file = os.path.join(self.target_folder, nef_file)

            if os.path.exists(source_file):
                shutil.copy2(source_file, target_file)
                print(f'文件 {nef_file} 已从 {self.source_folder} 拷贝到 {self.target_folder}')
            else:
                print(f'文件 {nef_file} 在 {self.source_folder} 中不存在')

        QMessageBox.information(self, "完成", "拷贝操作已完成！")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = NEFCopierApp()
    ex.show()
    sys.exit(app.exec_()) 