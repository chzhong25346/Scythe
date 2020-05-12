# -*- coding: utf-8 -*-
import logging
from Scythe.items import Enmax_Item
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from .models import db_connect, create_table, Enmax_load
from .mapping import map_enmax_load
logger = logging.getLogger('Pipeline')


class DBPipeline(object):

    def get_Db(self, dbname):
        e = db_connect(dbname)
        create_table(e)
        session = sessionmaker(bind=e)
        return session()


    def process_item(self, item, spider):
        # Enmax
        if isinstance(item, Enmax_Item):
            s = self.get_Db('learning')
            load = map_enmax_load(item)
            try:
                current_load = int(item['load'])
                today_entry = s.query(Enmax_load).filter_by(date=item['date']).first()
                if today_entry:
                    if current_load > today_entry.load:
                        today_entry.load = current_load
                        s.commit()
                    elif current_load <= today_entry.load:
                        pass
                else:
                    s.add(load)
                    s.commit()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
                # raise
            finally:
                s.close()
            return item
