# -*- coding: utf-8 -*-
import os
from .utils.config import Config
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

DeclarativeBase = declarative_base()

def db_connect(dbname):
    _USER = Config.DB_USER
    _PWD = Config.DB_PASS
    _PORT = Config.DB_PORT
    _HOST = Config.DB_HOST
    return create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'
                            .format(_USER, _PWD, _HOST, _PORT, dbname))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


# EIA Models
class Enmax_load(DeclarativeBase):
    __tablename__ = 'enmax_load'
    # id = Column('id', String(40), unique=True, nullable=False, primary_key=True)
    # tou = Column('tou', String(10), nullable=False)
    date = Column('date', DateTime, unique=True, nullable=False, primary_key=True)
    load = Column('load', Integer, nullable=True)


# Shpgx LNG Models
class ShpgxLng_load(DeclarativeBase):
    __tablename__ = 'shpgxlng_load'
    date = Column('date', DateTime, unique=True, nullable=False, primary_key=True)
    rmb_ton = Column('rmb_ton', Float, nullable=True)
    dollar_mmbtu = Column('dollar_mmbtu', Float, nullable=True)
    rmb_gj = Column('rmb_gj', Float, nullable=True)


# Psac Models
class Psac(DeclarativeBase):
    __tablename__ = 'psac'
    date = Column('date', DateTime, unique=True, nullable=False, primary_key=True)
    aeco = Column('aeco', Float, nullable=True)
    station2 = Column('station2', Float, nullable=True)
    dawn = Column('dawn', Float, nullable=True)
    henry_aeco_diff = Column('henry_aeco_diff', Float, nullable=True)
    henry = Column('henry', Float, nullable=True)
    wti = Column('wti', Float, nullable=True)
    wcs = Column('wcs', Float, nullable=True)
    wti_wcs_diff = Column('wti_wcs_diff', Float, nullable=True)


# Boe_US_rig
class Boe_US_rig(DeclarativeBase):
    __tablename__ = 'boe_us_rig'
    date = Column('date', DateTime, unique=True, nullable=False, primary_key=True)
    total = Column('total', Integer, nullable=True)
    eagle_ford = Column('eagle_ford', Integer, nullable=True)
    appalachian = Column('appalachian', Integer, nullable=True)
    permian = Column('permian', Integer, nullable=True)
    williston = Column('williston', Integer, nullable=True)
    dj_niobrara = Column('dj_niobrara', Integer, nullable=True)
    other_basins = Column('other_basins', Integer, nullable=True)
    oil = Column('oil', Integer, nullable=True)
    gas = Column('gas', Integer, nullable=True)


# Boe_CA_rig
class Boe_CA_rig(DeclarativeBase):
    __tablename__ = 'boe_ca_rig'
    date = Column('date', DateTime, unique=True, nullable=False, primary_key=True)
    total = Column('total', Integer, nullable=True)
    oil = Column('oil', Integer, nullable=True)
    gas = Column('gas', Integer, nullable=True)
    alberta = Column('alberta', Integer, nullable=True)
    bc = Column('bc', Integer, nullable=True)
    saskatchewan = Column('saskatchewan', Integer, nullable=True)
    manitoba = Column('manitoba', Integer, nullable=True)
    other_provinces = Column('other_provinces', Integer, nullable=True)