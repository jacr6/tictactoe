import seqlog
import logging
import json


class LogInfra(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self) -> None:
        """_summary_
        """
        seqlog.log_to_seq(
            server_url="http://my-seq-server:5341/",
            api_key="My API Key",
            level=logging.INFO,
            batch_size=10,
            auto_flush_timeout=10,  # seconds
            override_root_logger=True,
            # Optional; only specify this if you want to use a custom JSON encoder
            json_encoder_class=json.encoder.JSONEncoder
        )
        self.root_logger = logging.getLogger()
        pass

    def manage_error(self, fn, *args):
        try:
            fn(*args)
        except Exception as e:
            self.root_logger.error(f'ERROR on {fn.__name__}: {e.__str__()}')
