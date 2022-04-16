import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_monitor",
    version="0.0.1",
    author="Torres-圣君",
    author_email="2653644677@qq.com",
    description="基于NoneBot2实现，检测QQ群状态，例如：群成员人数变动、文件上传、红包运气王、管理员变动等",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjladmin/nonebot_plugin_monitor",
    license='MIT',
    install_requires=[
        "requests>=2.26.0",
        "nonebot2",
        "nonebot-adapter-onebot"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3'
)
