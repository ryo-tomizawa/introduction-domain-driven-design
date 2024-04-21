import os
import sys

current_dir = os.path.dirname(__file__)
circle_model_dir = os.path.abspath(os.path.join(current_dir, '../../../SnsDomain/Models/Circles'))
sys.path.append(circle_model_dir)

from typing import List
from circle import Circle
from circle_summary_date import CircleSummaryData

class CircleGetRecommendResult:
    def __init__(self, recommend_circles: List[Circle]) -> None:
        self.summaries = [CircleSummaryData(x) for x in recommend_circles]