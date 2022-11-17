from domain.report.credit import CreditReport
from domain.report.player import PlayerReport
from domain.report.profit import ProffitReport


class ReportDomain(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def __init__(self) -> None:
        """_summary_
        """
        self.credit_report = CreditReport()
        self.player_report = PlayerReport()
        self.profit_report = ProffitReport()
        pass
