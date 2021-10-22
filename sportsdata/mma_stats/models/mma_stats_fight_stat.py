# coding: utf-8

"""
    MMA v3 Stats

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MmaStatsFightStat(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fighter_id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'winner': 'bool',
        'fantasy_points': 'float',
        'fantasy_points_draft_kings': 'float',
        'knockdowns': 'float',
        'total_strikes_attempted': 'float',
        'total_strikes_landed': 'float',
        'sig_strikes_attempted': 'float',
        'sig_strikes_landed': 'float',
        'takedowns_attempted': 'float',
        'takedowns_landed': 'float',
        'takedowns_slams': 'float',
        'takedown_accuracy': 'float',
        'advances': 'float',
        'reversals': 'float',
        'submissions': 'float',
        'slam_rate': 'float',
        'time_in_control': 'float',
        'first_round_win': 'bool',
        'second_round_win': 'bool',
        'third_round_win': 'bool',
        'fourth_round_win': 'bool',
        'fifth_round_win': 'bool',
        'decision_win': 'bool'
    }

    attribute_map = {
        'fighter_id': 'FighterId',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'winner': 'Winner',
        'fantasy_points': 'FantasyPoints',
        'fantasy_points_draft_kings': 'FantasyPointsDraftKings',
        'knockdowns': 'Knockdowns',
        'total_strikes_attempted': 'TotalStrikesAttempted',
        'total_strikes_landed': 'TotalStrikesLanded',
        'sig_strikes_attempted': 'SigStrikesAttempted',
        'sig_strikes_landed': 'SigStrikesLanded',
        'takedowns_attempted': 'TakedownsAttempted',
        'takedowns_landed': 'TakedownsLanded',
        'takedowns_slams': 'TakedownsSlams',
        'takedown_accuracy': 'TakedownAccuracy',
        'advances': 'Advances',
        'reversals': 'Reversals',
        'submissions': 'Submissions',
        'slam_rate': 'SlamRate',
        'time_in_control': 'TimeInControl',
        'first_round_win': 'FirstRoundWin',
        'second_round_win': 'SecondRoundWin',
        'third_round_win': 'ThirdRoundWin',
        'fourth_round_win': 'FourthRoundWin',
        'fifth_round_win': 'FifthRoundWin',
        'decision_win': 'DecisionWin'
    }

    def __init__(self, fighter_id=None, first_name=None, last_name=None, winner=None, fantasy_points=None, fantasy_points_draft_kings=None, knockdowns=None, total_strikes_attempted=None, total_strikes_landed=None, sig_strikes_attempted=None, sig_strikes_landed=None, takedowns_attempted=None, takedowns_landed=None, takedowns_slams=None, takedown_accuracy=None, advances=None, reversals=None, submissions=None, slam_rate=None, time_in_control=None, first_round_win=None, second_round_win=None, third_round_win=None, fourth_round_win=None, fifth_round_win=None, decision_win=None):  # noqa: E501
        """MmaStatsFightStat - a model defined in Swagger"""  # noqa: E501
        self._fighter_id = None
        self._first_name = None
        self._last_name = None
        self._winner = None
        self._fantasy_points = None
        self._fantasy_points_draft_kings = None
        self._knockdowns = None
        self._total_strikes_attempted = None
        self._total_strikes_landed = None
        self._sig_strikes_attempted = None
        self._sig_strikes_landed = None
        self._takedowns_attempted = None
        self._takedowns_landed = None
        self._takedowns_slams = None
        self._takedown_accuracy = None
        self._advances = None
        self._reversals = None
        self._submissions = None
        self._slam_rate = None
        self._time_in_control = None
        self._first_round_win = None
        self._second_round_win = None
        self._third_round_win = None
        self._fourth_round_win = None
        self._fifth_round_win = None
        self._decision_win = None
        self.discriminator = None
        if fighter_id is not None:
            self.fighter_id = fighter_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if winner is not None:
            self.winner = winner
        if fantasy_points is not None:
            self.fantasy_points = fantasy_points
        if fantasy_points_draft_kings is not None:
            self.fantasy_points_draft_kings = fantasy_points_draft_kings
        if knockdowns is not None:
            self.knockdowns = knockdowns
        if total_strikes_attempted is not None:
            self.total_strikes_attempted = total_strikes_attempted
        if total_strikes_landed is not None:
            self.total_strikes_landed = total_strikes_landed
        if sig_strikes_attempted is not None:
            self.sig_strikes_attempted = sig_strikes_attempted
        if sig_strikes_landed is not None:
            self.sig_strikes_landed = sig_strikes_landed
        if takedowns_attempted is not None:
            self.takedowns_attempted = takedowns_attempted
        if takedowns_landed is not None:
            self.takedowns_landed = takedowns_landed
        if takedowns_slams is not None:
            self.takedowns_slams = takedowns_slams
        if takedown_accuracy is not None:
            self.takedown_accuracy = takedown_accuracy
        if advances is not None:
            self.advances = advances
        if reversals is not None:
            self.reversals = reversals
        if submissions is not None:
            self.submissions = submissions
        if slam_rate is not None:
            self.slam_rate = slam_rate
        if time_in_control is not None:
            self.time_in_control = time_in_control
        if first_round_win is not None:
            self.first_round_win = first_round_win
        if second_round_win is not None:
            self.second_round_win = second_round_win
        if third_round_win is not None:
            self.third_round_win = third_round_win
        if fourth_round_win is not None:
            self.fourth_round_win = fourth_round_win
        if fifth_round_win is not None:
            self.fifth_round_win = fifth_round_win
        if decision_win is not None:
            self.decision_win = decision_win

    @property
    def fighter_id(self):
        """Gets the fighter_id of this MmaStatsFightStat.  # noqa: E501


        :return: The fighter_id of this MmaStatsFightStat.  # noqa: E501
        :rtype: int
        """
        return self._fighter_id

    @fighter_id.setter
    def fighter_id(self, fighter_id):
        """Sets the fighter_id of this MmaStatsFightStat.


        :param fighter_id: The fighter_id of this MmaStatsFightStat.  # noqa: E501
        :type: int
        """

        self._fighter_id = fighter_id

    @property
    def first_name(self):
        """Gets the first_name of this MmaStatsFightStat.  # noqa: E501


        :return: The first_name of this MmaStatsFightStat.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MmaStatsFightStat.


        :param first_name: The first_name of this MmaStatsFightStat.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MmaStatsFightStat.  # noqa: E501


        :return: The last_name of this MmaStatsFightStat.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MmaStatsFightStat.


        :param last_name: The last_name of this MmaStatsFightStat.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def winner(self):
        """Gets the winner of this MmaStatsFightStat.  # noqa: E501


        :return: The winner of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this MmaStatsFightStat.


        :param winner: The winner of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._winner = winner

    @property
    def fantasy_points(self):
        """Gets the fantasy_points of this MmaStatsFightStat.  # noqa: E501


        :return: The fantasy_points of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points

    @fantasy_points.setter
    def fantasy_points(self, fantasy_points):
        """Sets the fantasy_points of this MmaStatsFightStat.


        :param fantasy_points: The fantasy_points of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._fantasy_points = fantasy_points

    @property
    def fantasy_points_draft_kings(self):
        """Gets the fantasy_points_draft_kings of this MmaStatsFightStat.  # noqa: E501


        :return: The fantasy_points_draft_kings of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._fantasy_points_draft_kings

    @fantasy_points_draft_kings.setter
    def fantasy_points_draft_kings(self, fantasy_points_draft_kings):
        """Sets the fantasy_points_draft_kings of this MmaStatsFightStat.


        :param fantasy_points_draft_kings: The fantasy_points_draft_kings of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._fantasy_points_draft_kings = fantasy_points_draft_kings

    @property
    def knockdowns(self):
        """Gets the knockdowns of this MmaStatsFightStat.  # noqa: E501


        :return: The knockdowns of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._knockdowns

    @knockdowns.setter
    def knockdowns(self, knockdowns):
        """Sets the knockdowns of this MmaStatsFightStat.


        :param knockdowns: The knockdowns of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._knockdowns = knockdowns

    @property
    def total_strikes_attempted(self):
        """Gets the total_strikes_attempted of this MmaStatsFightStat.  # noqa: E501


        :return: The total_strikes_attempted of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._total_strikes_attempted

    @total_strikes_attempted.setter
    def total_strikes_attempted(self, total_strikes_attempted):
        """Sets the total_strikes_attempted of this MmaStatsFightStat.


        :param total_strikes_attempted: The total_strikes_attempted of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._total_strikes_attempted = total_strikes_attempted

    @property
    def total_strikes_landed(self):
        """Gets the total_strikes_landed of this MmaStatsFightStat.  # noqa: E501


        :return: The total_strikes_landed of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._total_strikes_landed

    @total_strikes_landed.setter
    def total_strikes_landed(self, total_strikes_landed):
        """Sets the total_strikes_landed of this MmaStatsFightStat.


        :param total_strikes_landed: The total_strikes_landed of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._total_strikes_landed = total_strikes_landed

    @property
    def sig_strikes_attempted(self):
        """Gets the sig_strikes_attempted of this MmaStatsFightStat.  # noqa: E501


        :return: The sig_strikes_attempted of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._sig_strikes_attempted

    @sig_strikes_attempted.setter
    def sig_strikes_attempted(self, sig_strikes_attempted):
        """Sets the sig_strikes_attempted of this MmaStatsFightStat.


        :param sig_strikes_attempted: The sig_strikes_attempted of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._sig_strikes_attempted = sig_strikes_attempted

    @property
    def sig_strikes_landed(self):
        """Gets the sig_strikes_landed of this MmaStatsFightStat.  # noqa: E501


        :return: The sig_strikes_landed of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._sig_strikes_landed

    @sig_strikes_landed.setter
    def sig_strikes_landed(self, sig_strikes_landed):
        """Sets the sig_strikes_landed of this MmaStatsFightStat.


        :param sig_strikes_landed: The sig_strikes_landed of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._sig_strikes_landed = sig_strikes_landed

    @property
    def takedowns_attempted(self):
        """Gets the takedowns_attempted of this MmaStatsFightStat.  # noqa: E501


        :return: The takedowns_attempted of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._takedowns_attempted

    @takedowns_attempted.setter
    def takedowns_attempted(self, takedowns_attempted):
        """Sets the takedowns_attempted of this MmaStatsFightStat.


        :param takedowns_attempted: The takedowns_attempted of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._takedowns_attempted = takedowns_attempted

    @property
    def takedowns_landed(self):
        """Gets the takedowns_landed of this MmaStatsFightStat.  # noqa: E501


        :return: The takedowns_landed of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._takedowns_landed

    @takedowns_landed.setter
    def takedowns_landed(self, takedowns_landed):
        """Sets the takedowns_landed of this MmaStatsFightStat.


        :param takedowns_landed: The takedowns_landed of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._takedowns_landed = takedowns_landed

    @property
    def takedowns_slams(self):
        """Gets the takedowns_slams of this MmaStatsFightStat.  # noqa: E501


        :return: The takedowns_slams of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._takedowns_slams

    @takedowns_slams.setter
    def takedowns_slams(self, takedowns_slams):
        """Sets the takedowns_slams of this MmaStatsFightStat.


        :param takedowns_slams: The takedowns_slams of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._takedowns_slams = takedowns_slams

    @property
    def takedown_accuracy(self):
        """Gets the takedown_accuracy of this MmaStatsFightStat.  # noqa: E501


        :return: The takedown_accuracy of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._takedown_accuracy

    @takedown_accuracy.setter
    def takedown_accuracy(self, takedown_accuracy):
        """Sets the takedown_accuracy of this MmaStatsFightStat.


        :param takedown_accuracy: The takedown_accuracy of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._takedown_accuracy = takedown_accuracy

    @property
    def advances(self):
        """Gets the advances of this MmaStatsFightStat.  # noqa: E501


        :return: The advances of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._advances

    @advances.setter
    def advances(self, advances):
        """Sets the advances of this MmaStatsFightStat.


        :param advances: The advances of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._advances = advances

    @property
    def reversals(self):
        """Gets the reversals of this MmaStatsFightStat.  # noqa: E501


        :return: The reversals of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._reversals

    @reversals.setter
    def reversals(self, reversals):
        """Sets the reversals of this MmaStatsFightStat.


        :param reversals: The reversals of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._reversals = reversals

    @property
    def submissions(self):
        """Gets the submissions of this MmaStatsFightStat.  # noqa: E501


        :return: The submissions of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this MmaStatsFightStat.


        :param submissions: The submissions of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._submissions = submissions

    @property
    def slam_rate(self):
        """Gets the slam_rate of this MmaStatsFightStat.  # noqa: E501


        :return: The slam_rate of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._slam_rate

    @slam_rate.setter
    def slam_rate(self, slam_rate):
        """Sets the slam_rate of this MmaStatsFightStat.


        :param slam_rate: The slam_rate of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._slam_rate = slam_rate

    @property
    def time_in_control(self):
        """Gets the time_in_control of this MmaStatsFightStat.  # noqa: E501


        :return: The time_in_control of this MmaStatsFightStat.  # noqa: E501
        :rtype: float
        """
        return self._time_in_control

    @time_in_control.setter
    def time_in_control(self, time_in_control):
        """Sets the time_in_control of this MmaStatsFightStat.


        :param time_in_control: The time_in_control of this MmaStatsFightStat.  # noqa: E501
        :type: float
        """

        self._time_in_control = time_in_control

    @property
    def first_round_win(self):
        """Gets the first_round_win of this MmaStatsFightStat.  # noqa: E501


        :return: The first_round_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._first_round_win

    @first_round_win.setter
    def first_round_win(self, first_round_win):
        """Sets the first_round_win of this MmaStatsFightStat.


        :param first_round_win: The first_round_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._first_round_win = first_round_win

    @property
    def second_round_win(self):
        """Gets the second_round_win of this MmaStatsFightStat.  # noqa: E501


        :return: The second_round_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._second_round_win

    @second_round_win.setter
    def second_round_win(self, second_round_win):
        """Sets the second_round_win of this MmaStatsFightStat.


        :param second_round_win: The second_round_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._second_round_win = second_round_win

    @property
    def third_round_win(self):
        """Gets the third_round_win of this MmaStatsFightStat.  # noqa: E501


        :return: The third_round_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._third_round_win

    @third_round_win.setter
    def third_round_win(self, third_round_win):
        """Sets the third_round_win of this MmaStatsFightStat.


        :param third_round_win: The third_round_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._third_round_win = third_round_win

    @property
    def fourth_round_win(self):
        """Gets the fourth_round_win of this MmaStatsFightStat.  # noqa: E501


        :return: The fourth_round_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._fourth_round_win

    @fourth_round_win.setter
    def fourth_round_win(self, fourth_round_win):
        """Sets the fourth_round_win of this MmaStatsFightStat.


        :param fourth_round_win: The fourth_round_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._fourth_round_win = fourth_round_win

    @property
    def fifth_round_win(self):
        """Gets the fifth_round_win of this MmaStatsFightStat.  # noqa: E501


        :return: The fifth_round_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._fifth_round_win

    @fifth_round_win.setter
    def fifth_round_win(self, fifth_round_win):
        """Sets the fifth_round_win of this MmaStatsFightStat.


        :param fifth_round_win: The fifth_round_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._fifth_round_win = fifth_round_win

    @property
    def decision_win(self):
        """Gets the decision_win of this MmaStatsFightStat.  # noqa: E501


        :return: The decision_win of this MmaStatsFightStat.  # noqa: E501
        :rtype: bool
        """
        return self._decision_win

    @decision_win.setter
    def decision_win(self, decision_win):
        """Sets the decision_win of this MmaStatsFightStat.


        :param decision_win: The decision_win of this MmaStatsFightStat.  # noqa: E501
        :type: bool
        """

        self._decision_win = decision_win

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MmaStatsFightStat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MmaStatsFightStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other