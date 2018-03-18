import Tkinter;
import os;


# Classes

class entity(object):
    def idSetter(self):
        self.ID = "";

    def nameSetter(self):
        self.name = "";


class archive(object):
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


# Methods
def main():
    main_window = App();


# eventScrivner - returns a dictionary of events, events read from a file called events.txt
def eventScrivner():
    path = os.getcwd();
    inFile = open(path + "\\events.txt", "r");
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
    path = os.getcwd();
    inFile = open(path + "\\nodes.txt", "r");
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
    path = os.getcwd();
    inFile = open(path + "\\scenes.txt", "r");
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
    path = os.getcwd();
    inFile = open(path + "\\rooms.txt", "r");
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
        # Main Window Related:
        self.main_window = Tkinter.Tk();
        self.main_window.geometry("1120x600");
        self.mainTextString = Tkinter.StringVar();
        self.secTextString = Tkinter.StringVar();
        self.roomTextString = Tkinter.StringVar();
        # Frame Related
        # Border decoration. The default is FLAT. Other possible values are SUNKEN, RAISED, GROOVE, and RIDGE.
        self.titleFrame = Tkinter.Frame(self.main_window, borderwidth=5, relief="groove");
        self.titleFrame.grid(row=0, column=0, padx=10, pady=5, sticky='w');

        # Main Text Frame
        self.textFrame = Tkinter.Frame(self.main_window, borderwidth=5, relief="groove", width=1100, height=500);
        self.textFrame.grid(row=2, column=0, columnspan=6, padx=10, pady=5, sticky=("w", "e"));

        # Choice Frame
        self.choiceFrame = Tkinter.Frame(self.main_window, borderwidth=5, relief="groove");
        self.choiceFrame.grid(row=4, column=0, columnspan=6, padx=10, pady=5, sticky=("w", "e"))

        # Input Frame
        self.interactionFrame = Tkinter.Frame(self.main_window);
        self.interactionFrame.grid(row=5, column=0, sticky=("w"), padx=10);

        # Label Related
        self.titleLabel = Tkinter.Label(self.titleFrame, text="A BRIEF EXCHANGE", width=16);
        self.titleLabel.config(font=("Cambria", 24));
        self.titleLabel.pack(side="left");

        self.choiceLabel = Tkinter.Label(self.main_window, text="Your Choices:")
        self.choiceLabel.config(font=("Cambria", 16));
        self.choiceLabel.grid(row=3, column=0, sticky="w", padx=10);

        self.choiceLabel = Tkinter.Label(self.main_window, textvariable=self.roomTextString)
        self.choiceLabel.config(font=("Cambria", 16));
        self.choiceLabel.grid(row=1, column=0, sticky=("w"), padx=10);

        # Text Related11
        self.mainText = Tkinter.Message(self.textFrame, width=1090, textvariable=self.mainTextString);
        self.mainText.config(font=("Cambria", 18));
        self.mainText.grid(row=0, column=0, sticky=("w"));

        self.secText = Tkinter.Message(self.choiceFrame, width=1090, textvariable=self.secTextString)
        self.secText.config(font=("Cambria", 16));
        self.secText.grid(row=0, column=0, sticky=("w"), padx=10);

        # Input Related
        self.entry = Tkinter.Entry(self.interactionFrame, width=10);
        self.entry.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"));
        self.entry.grid(row=0, column=0);
        self.contBut = Tkinter.Button(self.interactionFrame, text="Engage", command=self.activate);
        self.contBut.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"));
        self.contBut.grid(row=0, column=1);
        self.quit = Tkinter.Button(self.interactionFrame, text="Quit", command=self.main_window.destroy);
        self.quit.config(relief="groove", borderwidth=2, font=("Cambria", 18, "bold"))
        self.quit.grid(row=0, column=2);

        console = "";
        self.arch = archive();
        self.arch.currentRoomSetter();
        self.arch.events = eventScrivner();
        self.arch.nodes = nodeScrivner(self.arch);
        self.arch.scenes = sceneScrivner(self.arch);
        self.arch.rooms = roomScrivner(self.arch);
        self.load(self.arch, self.arch.currentRoom);
        # while console != "q":
        #    load(arch,arch.currentRoom);
        #    console = input("\nWhat do you do?\n");
        #
        Tkinter.mainloop();

    def activate(self):
        ourArchive = self.arch;
        playerInput = self.entry.get();
        # self.mainTextString.set(playerInput);
        self.load(ourArchive, ourArchive.currentRoom);
        try:
            choiceNum = int(playerInput);
            # playerChoice translates choice num into the
            # index of the option the player selected.
            playerChoice = int(choiceNum) - 1;
            theScene = ourArchive.rooms[ourArchive.currentRoom].roomScenes[
                ourArchive.rooms[ourArchive.currentRoom].currentScene]
            if playerChoice == len(theScene.sceneNodes):
                if theScene.examine != "":
                    self.mainTextString.set(theScene.examine);
                    self.entry.delete(0, 10);
                else:
                    self.mainTextString.set("The range was off. There is/are only " + str(len(
                        theScene.sceneNodes)) + " choices in this scene, not including an examine option. Clear the entry box and hit continue to return to the previous scene.");
                    self.entry.delete(0, 10);
            else:
                theScene.sceneNodes[playerChoice].activateNode(ourArchive);
                self.load(self.arch, self.arch.currentRoom);
                self.entry.delete(0, 10);

        except ValueError:
            if playerInput == "":
                self.load(self.arch, self.arch.currentRoom);
                self.entry.delete(0, 10);
            else:
                self.mainTextString.set("Please enter the number of the option you want.");
                self.entry.delete(0, 10);
        except IndexError:
            self.mainTextString.set("The range was off. There is/are only " + str(len(
                theScene.sceneNodes)) + " choices in this scene, not including an examine option. Clear the entry box and hit continue to return to the previous scene.");
            self.entry.delete(0, 10);

    def load(self, loadArch, loadArchRoom):
        thisRoom = loadArch.rooms[loadArchRoom];
        thisScene = thisRoom.roomScenes[thisRoom.currentScene];
        secText = "";
        self.roomTextString.set(thisScene.name);
        self.mainTextString.set(thisScene.text);
        num = 1;
        for i in range(0, len(thisScene.sceneNodes)):
            secText += ("\t" + str(i + 1) + ": " + thisScene.sceneNodes[i].name + "\n");
            num += 1;
        if thisScene.examine != "":
            secText += ("\t" + str(num) + ": Examine.");
        self.secTextString.set(secText);
main();
