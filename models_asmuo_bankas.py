from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/asmuo_bankas.db')
Base = declarative_base()


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asmens_kodas = Column("asmens kodas", Integer, unique=True)
    tel_nr = Column("telefono numeris", Integer)

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde},{self.asmens_kodas}, {self.tel_nr})"


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    banko_kodas = Column("banko kodas", Integer)
    swift_kodas = Column("SWIFT kodas", String)

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.adresas}, {self.banko_kodas}, {self.swift_kodas})"


class Saskaita(Base):
    __tablename__ = "saskaita"
    id = Column(Integer, primary_key=True)
    numeris = Column("saskaitos numeris", String)
    balansas = Column("saskaitos balansas", Float)
    asmuo_id = Column("asmuo_id", Integer, ForeignKey("asmuo.id"))
    asmuo = relationship("Asmuo")
    bankas_id = Column("bankas_id", Integer, ForeignKey("bankas.id"))
    bankas = relationship("Bankas")

    def __repr__(self):
        return f"({self.id}, {self.numeris}, {self.balansas}, {self.asmuo}, {self.bankas})"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)