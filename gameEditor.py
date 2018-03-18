# Allows you to edit the game through an interface.

import tkinter

class entity(object):
    def idSetter(self):
        self.ID = "";

    def nameSetter(self):
        self.name = "";


class archive(object):
    # List of dictionary keys
    def refListSetter(self):
        self.refList = [];
        self.roomList = [];
        self.sceneList = [];
        self.nodeList = [];
        self.eventList = [];
        self.refList.append(self.roomList);
        self.refList.append(self.sceneList);
        self.refList.append(self.nodeList);
        self.refList.append(self.eventList);

    def currentRoomSetter(self):
        self.currentRoom = "room0";

    def eventsDict(self):
        self.events = {};

    def nodesDict(self):
        self.nodes = {};

    def scenesDict(self):
        self.scenes = {};

    def roomsDict(self):
        self.rooms = {};


# room - room inherits from entity giving it a name and an id. Rooms are what the player interacts
# with directly. They contain scenes which the player sees. For example, room1 may be called "The Grato"
# in the first scene of "The Grato" the player encounters a gang of pirates, in the second scene of
# The Grato the player may have dealt with the pirates and now the Grato is empty.
class room(entity):
    def sceneSetter(self):
        self.roomScenes = [];

    def currentSceneSetter(self):
        self.currentScene = 0;


# scene - scene inherits from entity giving it a name and an id. It contains a list of nodes which the player
# can interact with, as well as a description of the room it takes place in.
class scene(entity):
    def textSetter(self):
        self.text = "";

    def nodeSetter(self):
        self.sceneNodes = [];

    def examSetter(self):
        self.examine = "";


class node(entity):
    def eventsSetter(self):
        self.nodeEvents = [];

    def activateNode(self, arch):
        for i in range(len(self.nodeEvents)):
            self.nodeEvents[i].activate(arch);


class event(entity):
    def activeSetter(self):
        self.active = "";

    def activate(self, arch):
        # Test in Code
        parsedEffect = self.active.split();
        # swap roomID sceneID
        if parsedEffect[0] == "swap":
            roomRef = arch.rooms[parsedEffect[1]];
            roomRef.currentScene = int(parsedEffect[2]);
        if parsedEffect[0] == "goto":
            arch.currentRoom = parsedEffect[1];
        if parsedEffect[0] == "print":
            print(parsedEffect[1]);
        if parsedEffect[0] == "node":
            # node roomID sceneID nodeNumber eventNum NewEventID
            roomRef = arch.rooms[parsedEffect[1]];
            activeNode = roomRef.roomScenes[int(parsedEffect[2])].sceneNodes[int(parsedEffect[3])];
            activeNode.name = self.name;
            activeNode.nodeEvents[int(parsedEffect[4])] = arch.events[parsedEffect[5]];


# eventScrivner - returns a dictionary of events, events read from a file called events.txt
def eventScrivner(archEvents):
    inFile = open("events.txt", "r");
    line = inFile.readline().rstrip();
    events = {};
    while line != "ENDEVENTS":
        line = inFile.readline().rstrip();
        tempEvent = event();
        tempEvent.idSetter();
        tempEvent.nameSetter();
        tempEvent.activeSetter();
        while line != "endevent" and line != "ENDEVENTS":
            # print(line);
            if line[0:5] == "id  :":
                tempEvent.ID = line[6:];
                archEvents.refList[3].append(tempEvent.ID);
            if line[0:5] == "name:":
                tempEvent.name = line[6:];
            if line[0:5] == "acti:":
                tempEvent.active = line[6:];
            line = inFile.readline().rstrip();
        events[tempEvent.ID] = tempEvent;
    inFile.close();
    return events;


# nodeScrivner - returns a dictionary of nodes.
def nodeScrivner(archNodes):
    inFile = open("nodes.txt", "r");
    line = inFile.readline().rstrip();
    nodes = {};
    while line != "ENDNODES":
        # print(line);
        line = inFile.readline().rstrip();
        tempNode = node();
        tempNode.idSetter();
        tempNode.nameSetter();
        tempNode.eventsSetter();
        while line != "endnode" and line != "ENDNODES":
            if line[0:5] == "id  :":
                tempNode.ID = line[6:];
            if line[0:5] == "name:":
                tempNode.name = line[6:];
            if line[0:5] == "even:":
                line = inFile.readline().rstrip();
                while line != "endeven":
                    # print(line);
                    tempNode.nodeEvents.append(archNodes.events[line]);
                    line = inFile.readline().rstrip();
            line = inFile.readline().rstrip();
        nodes[tempNode.ID] = tempNode;
    inFile.close();
    return nodes;


def sceneScrivner(archScenes):
    inFile = open("scenes.txt", "r");
    line = inFile.readline().rstrip();
    scenes = {};
    while line != "ENDSCENES":
        line = inFile.readline().rstrip();
        tempScene = scene();
        tempScene.idSetter();
        tempScene.nameSetter();
        tempScene.textSetter();
        tempScene.nodeSetter();
        tempScene.examSetter();
        while line != "endscene" and line != "ENDSCENES":
            if line[0:5] == "id  :":
                tempScene.ID = line[6:];
            if line[0:5] == "name:":
                tempScene.name = line[6:];
            if line[0:5] == "text:":
                tempScene.text = line[6:];
            if line[0:5] == "exam:":
                tempScene.examine = line[6:];
            if line[0:5] == "node:":
                line = inFile.readline().rstrip();
                while line != "endnodes":
                    # print(line);
                    tempScene.sceneNodes.append(archScenes.nodes[line]);
                    line = inFile.readline().rstrip();
            line = inFile.readline().rstrip();
        scenes[tempScene.ID] = tempScene;
    inFile.close();
    return scenes;


def roomScrivner(archRooms):
    inFile = open("rooms.txt", "r");
    line = inFile.readline().rstrip();
    rooms = {};
    while line != "ENDROOMS":
        line = inFile.readline().rstrip();
        tempRoom = room();
        tempRoom.idSetter();
        tempRoom.nameSetter();
        tempRoom.sceneSetter();
        tempRoom.currentSceneSetter();
        while line != "endroom" and line != "ENDROOMS":
            if line[0:5] == "id  :":
                tempRoom.ID = line[6:];
            if line[0:5] == "name:":
                tempRoom.name = line[6:];
            if line[0:5] == "scen:":
                line = inFile.readline().rstrip();
                while line != "endscenes":
                    # print(line);
                    tempRoom.roomScenes.append(archRooms.scenes[line]);
                    line = inFile.readline().rstrip();
            line = inFile.readline().rstrip();
        rooms[tempRoom.ID] = tempRoom;
    inFile.close();
    return rooms;

class App:
    def __init__(self):
        self.arch = archive();
        self.arch.currentRoomSetter();
        self.arch.events = eventScrivner(self.arch);
        self.arch.nodes = nodeScrivner(self.arch);
        self.arch.scenes = sceneScrivner(self.arch);
        self.arch.rooms = roomScrivner(self.arch);
        self.arch.refListSetter();




    def roomWrite(self, newRoom):
        f = open("rooms.txt","r");
        newRoomsDoc = "";
        line = f.readline();
        while line != "ENDROOMS":
            newRoomsDoc += line;
            line = f.readline();
        # Transcribes the new room onto the textfile
        newRoomsDoc += "\n";
        # Adds the id to the new room
        newRoomsDoc += "id  : " + str(newRoom.ID) + "\n";
        # Adds the name
        newRoomsDoc += "name: " + str(newRoom.name) + "\n";
        # Creates scenes sub folder
        newRoomsDoc += "scen:\nendscenes\n";
        # Closes the scene and closes the rooms file
        newRoomsDoc += "endroom\nENDROOMS"
        f.close();
        out = open("rooms.txt","w");
        out.write(newRoomsDoc);
        out.close();

    def sceneWrite(self, newScene, parentRoom):
        f = open("scenes.txt","r");
        newScenesDoc = "";
        line = f.readline();
        while line != "ENDSCENES":
            newScenesDoc += line;
            line = f.readline();
        # Transcribes the new room onto the textfile
        newScenesDoc += "\n";
        # Adds the id to the new room
        newScenesDoc += "id  : " + str(newScene.ID) + "\n";
        # Adds the name
        newScenesDoc += "name: " + str(newScene.name) + "\n";
        # Creates the text
        newScenesDoc += "text: " + str(newScene.text) + "\n";
        # Creates the examine text
        newScenesDoc += "exam:";
        if newScene.examine != "":
            newScenesDoc += str(newScene.text) + "\n"
        else:
            newScenesDoc += "\n";
        # Creates nodes sub folder
        newScenesDoc += "node:\nendnodes\n";
        # Closes the scene and closes the rooms file
        newScenesDoc += "endscene\nENDSCENES"
        f.close();
        out = open("scenes.txt","w");
        out.write(newScenesDoc);
        out.close();


main = App();