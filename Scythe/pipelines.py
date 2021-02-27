# -*- coding: utf-8 -*-
import logging
from Scythe.items import Enmax_Item, ShpgxLng_Item, Psac_Item, Boe_US_rig_Item, Boe_CA_rig_Item, CIBC_metals_Item
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from .models import db_connect, create_table, Enmax_load, ShpgxLng_load, Psac, Boe_US_rig, Boe_CA_rig, CIBC_metals
from .mapping import map_enmax_load, map_shpgxLng_load, map_psac, map_boe_us_rig, map_boe_ca_rig, map_cibc_metals
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

        # Shpgx LNG
        elif isinstance(item, ShpgxLng_Item):
            s = self.get_Db('learning')
            load = map_shpgxLng_load(item)
            try:
                s.add(load)
                s.commit()
            except exc.IntegrityError:
                s.rollback()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
            finally:
                s.close()
            return item

        # PSAC
        elif isinstance(item, Psac_Item):
            s = self.get_Db('learning')
            data = map_psac(item)
            try:
                s.add(data)
                s.commit()
            except exc.IntegrityError:
                s.rollback()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
            finally:
                s.close()
            return item

        # Boe_US_rig
        elif isinstance(item, Boe_US_rig_Item):
            s = self.get_Db('learning')
            data = map_boe_us_rig(item)
            try:
                s.add(data)
                s.commit()
            except exc.IntegrityError:
                s.rollback()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
            finally:
                s.close()
            return item

        # Boe_CA_rig
        elif isinstance(item, Boe_CA_rig_Item):
            s = self.get_Db('learning')
            data = map_boe_ca_rig(item)
            try:
                s.add(data)
                s.commit()
            except exc.IntegrityError:
                s.rollback()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
            finally:
                s.close()
            return item

        # CIBC metals
        elif isinstance(item, CIBC_metals_Item):
            s = self.get_Db('learning')
            data = map_cibc_metals(item)
            try:
                s.add(data)
                s.commit()
            except exc.IntegrityError:
                s.rollback()
            except:
                s.rollback()
                logger.error("DB failure: %s" % str(item))
            finally:
                s.close()
            return item
