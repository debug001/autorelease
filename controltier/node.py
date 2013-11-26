#encoding=utf-8
__author__ = 'jophyyao'

from base import Base
import re, os, sys


class Node(Base):
    type       =   "Node"
    ctlUsername=   "apps"
    osFamily   =   "unix"
    osName     =   "Linux"
    osArch     =   "x86_64"
    osVersion  =   "5.8"
    ctlBase    =   ""
    ctlHome    =   ""


    def __init__(self, project, file="/tmp/node.txt"):
        super(Node, self).__init__()
        self.project = project
        self.file    = file

    def node_count(self):
        index = 0
        regex = re.compile(r"^\s*<node type", re.I)
        for row in open("%s" % self.ROOT + "/ctl/projects/" + self.project + "/etc/resources.xml", "r"):
            if re.search(regex, row):
                index += 1
        return index

    def tag_exist_count(self):
        index = 0
        regex = re.compile(r"tags=[\"'](.+?)[\"']", re.I)
        for row in open("%s" % self.ROOT + "/ctl/projects/" + self.project + "/etc/resources.xml", "r"):
            if "tags" in row:
                if re.search(regex, row).group(1) == "p1":
                    index += 1
        return index


    def create(self):
        tag_p1_no = 0
        node_count = self.node_count()
        tag_count = node_count/100 + 1                 #tag all
        tag_p1_count = self.tag_exist_count()          #p1

        #print node_count, tag_count, tag_p1_count

        if tag_p1_count < tag_count:
            tag_p1_no = tag_count - tag_p1_count

        xml_contents = """
        <!DOCTYPE project PUBLIC "-//ControlTier Software Inc.//DTD Project Document 1.0//EN" "project.dtd">
            <project>
        """

        for row in open(self.file, "r"):
            row = row.strip()
            if not row: continue
            row = row.split()

            if len(row) < 3 and len(row) > 1:
                row.append("")
            hostname, ip, description = row[0:3]

            if tag_count > 0:
                tag = "p1"
                tag_count -= 1
            else:
                tag = "p100"

            xml_contents += """
              <node type="%s" name="%s" description="%s" tags="%s" ctlBase="%s" ctlHome="%s" ctlUsername="%s" osFamily="%s" osName="%s" osArch="%s" osVersion="%s" hostname="%s"/>
           """
            xml_contents %= (
                self.type,
                hostname,
                description,
                tag,
                self.ctlBase,
                self.ctlHome,
                self.ctlUsername,
                self.osFamily,
                self.osName,
                self.osArch,
                self.osVersion,
                ip,
            )

        xml_contents += """
           </project>
        """

        f = open("temp.xml", "w")
        f.write(xml_contents)
        f.close()

        os.system("/usr/local/ctier/pkgs/ctl-3.6.1/bin/ctl -p %s -m ProjectBuilder -c load-resources -- -filename temp.xml" % self.project)



    def analysis(self):
        import xml.dom.minidom

        result = {}
        index = 1

        resources_file = os.path.join(self.ROOT, "ctl/projects", self.project, "etc") + '/resources.xml'
        doc = xml.dom.minidom.parseString(open(resources_file, "r").read())
        for node in doc.getElementsByTagName("node"):
            result[index] = {}
            result[index]['name'] = node.getAttribute('name')
            result[index]['description'] = node.getAttribute('description')
            result[index]['tags'] = node.getAttribute('tags')
            result[index]['ctlUsername'] = node.getAttribute('ctlUsername')
            result[index]['osFamily'] = node.getAttribute('osFamily')
            result[index]['osName'] = node.getAttribute('osName')
            result[index]['osArch'] = node.getAttribute('osArch')
            result[index]['osVersion'] = node.getAttribute('osVersion')
            result[index]['hostname'] = node.getAttribute('hostname')

            index +=1
        return result





















