from setuptools import find_packages, setup

name = 'vebench'

long_description='Please refer to https://github.com/littlespray/VE-Bench'

setup(
    name=name,  # 包名同工程名，这样导入包的时候更有对应性
    version='1.0.0',
    author="Shangkun Sun",
    license="MIT Licence",
    author_email='sunshk@stu.pku.edu.cn',
    description="Evaluator for Text-driven Video Editing",
    packages=find_packages(),
    python_requires='>=3',
    long_description=long_description,    
    # 设置依赖包
    install_requires=['torch', 'decord', 'einops', 'fairscale', 'numpy', 'timm', 'transformers', 'sk-video'],
    include_package_data=True,  # 包含额外的非Python文件
    package_data={
        '': ['configs/*.yaml', 'models/backbone/BLIP_configs/*'],  # 匹配目录下的所有文件
    },
)
