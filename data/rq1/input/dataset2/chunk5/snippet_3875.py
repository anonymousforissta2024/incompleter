#Source: https://stackoverflow.com/questions/60360550/sqlalchemy-multiple-nested-queries-with-filters-from-one-table-attributeerror
poste_eu = db.session.query(
    (Sale.id, Sale.poste, Sale.pays).filter(or_(Sale.pays=='United Kingdom', Sale.pays=='France', Sale.pays=='Germany',\
           Sale.pays=='The Netherlands', Sale.pays=='Italy', Sale.pays=='Slovakia', Sale.pays=='Ireland',\
           Sale.pays=='Malta', Sale.pays=='Belgium', Sale.pays=='Spain')).label('poste_eu')
    ).group_by(Sale.id.asc()).subquery()