# Copyright Contributors to the OpenTimelineIO project
#
# SPDX-License-Identifier: Apache-2.0
#

import io
import setuptools

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


"""
OpenTimelineIO plugin adapter for .drp files created by the Blackmagic ATEM ISO
"""

setuptools.setup(
    name="otio-drp-adapter",
    author="Gilou",
    author_email="contact+dev@gilouweb.com",
    version="0.2.1",
    description="OpenTimelineIO adapter plugin for .drp files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gilou/otio-drp-adapter",
    packages=setuptools.find_packages(),
    entry_points={
        "opentimelineio.plugins": "otio_drp_adapter = otio_drp_adapter"
    },
    package_data={
        "otio_drp_adapter": [
            "plugin_manifest.json",
        ],
    },
    install_requires=["OpenTimelineIO >= 0.12.0"],
    extras_require={"dev": ["flake8", "pytest", "twine"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
    ],
)
