# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import Stack
from game import Directions, Actions
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

$ANSIBLE_VAULT;1.1;AES256
39393838383638383530363432663236636337336266623536643466653937303434633461663465
3034393930326534613731633335363830383831366539620a663132366566303161646236643237
33636363613331313530646561303731326231323566613130633937333963666635353634336264
6464343962616530390a663461303736646462383261656334316435633435396363373333353834
61646431393332363437653836353137313166376562316533633235643566363538666337613964
62616365666663373734373961346465326532623134616465313139396434343631636332326137
61353131363230616132666631383163396663356130383236346564653331363235323561383938
33633839613735656133383437373538356438633736363566363637643962666536386332303964
63323130346230333532346539366632303531343064306535323632663030646534363161383364
36613336343062613438653937393737643238666463363365363864353165396533383362383331
61613864646461346639383538333830613131646266343861623433326630323434323839383765
30343164663161303434353637343831643566636335306638323438643139363765656263643065
33663132613665306235323861306335363132613138626661343635383866656562356564643764
64386261313939636235356164313635383535653432636636646139373438633932363433626662
34653564613866656364623561386661656437626635633035633838383632366235636263393261
30323362313864643262366462343263643337323163613365656234376166383536626238363635
65643938653037356634663439333961313334383431343535643331653362616362396462363964
36323539613438373030636664633664366236653439323365353064363936656437366266306264
65336236306364636537663034643536633639356336653062663131393335383233333061313630
39363163396464303237383963363038363033653439346335653263613238666261333565663232
63303265643439303664393032383434373530643964313336313161626666383634633632343364
38383534636161616239393261363838323234353730326237333366363035393864313330306166
61343861353165323835343461383337366332303931636361363038353866373039323235356336
66643931323866383131616231333635353235303265303362313966303163343333306432326462
36646261326531613333356332343662653965346664356436363063326232376561666138356533
64353164313631663530373039356433306239366233343539646663323230663533313330343133
33663435663462396339623239353336303763396363396438376239373164666664636161613566
39656435653264376431393838326335386532333631336630303832663064653335343130663261
37653831326538306631366239636131366233353431373061366261383864343032336536353864
63363238313938366232643237356163626431643135613135393538646563653136316164373134
643339613430383461663432303633383362

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
