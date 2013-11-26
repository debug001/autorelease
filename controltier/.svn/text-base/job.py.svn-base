#encoding=utf-8
__author__ = 'jophyyao'

from base import Base
import os

class Job(Base):
    """
    project, group
    """
    loglevel = "INFO"
    threadcount = 1
    tags = ""
    keepgoing = "false"

    option_contents = ""
    script_contents = ""

    def __init__(self, configs):
        configs.setdefault("description", "")
        configs.setdefault("group", "")
        configs.setdefault("option", {})
        if configs.has_key('threadcount'):
            self.threadcount = int(configs['threadcount'])
        if configs.has_key('tags'):
            self.tags = configs['tags']

        self.configs = configs

    def option(self, name, default="", desc=""):
        option_contents = """
            <option name='{name}' enforcedvalues='false' required='true' default="{default}" description='{description}' />
        """.format(
            name = name,
            default = default,
            description = desc,
        )
        self.option_contents += option_contents

    def script(self, script_file="E:\py_project\controltier\script.txt"):
        if os.path.isfile(script_file):
            f = open(script_file, "r")
            contents = f.read()
            self.script_contents = contents
        else:
            raise("can not find script_file!")

    def create(self):
        if self.option_contents:
            option_start = "<options>"
            option_end   = "</options>"
        else:
            option_start, option_end = "", ""

        self.script()

        if self.script_contents:
            script_start = """
            <command>
                <script>
            """
            script_end   = """
                ]]></script>
                <scriptargs></scriptargs>
            </command>
            """
        else:
            script_start, script_end = "", ""



        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <joblist>
            <job>
            <name>{project}</name>
            <description>{description}</description>
            <additional/>
            <loglevel>{loglevel}</loglevel>
            <group>{group}</group>
            <context>
                <project>{project2}</project>
                {option_start}
                    {option_contents}
                {option_end}
            </context>
            <sequence threadcount="{threadcount}" keepgoing="false" strategy="node-first">
            {script_start}<![CDATA[
                {script_contents}
            {script_end}
            </sequence>
            <nodefilters excludeprecedence="true">
            <include>
                <tags>{tags}</tags>
            </include>
            </nodefilters>
            <dispatch>
                <threadcount>{threadcount2}</threadcount>
                <keepgoing>{keepgoing}</keepgoing>
            </dispatch>
            </job>
        </joblist>
        """.format(
            project = self.configs['project'],
            description = self.configs['description'],
            loglevel = self.loglevel,
            group = self.configs['group'],
            project2 = self.configs['project'],
            option_start = option_start,
            option_contents = self.option_contents,
            option_end = option_end,
            threadcount = self.threadcount,
            script_start = script_start ,
            script_contents = self.script_contents,
            script_end = script_end,
            tags = self.tags,
            threadcount2 = self.threadcount,
            keepgoing = self.keepgoing,

        )


        print xml
