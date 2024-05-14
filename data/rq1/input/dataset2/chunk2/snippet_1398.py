#Source: https://stackoverflow.com/questions/72119681/attributeerror-could-not-locate-column-in-row-for-column-sa-instance-state-f
class Clientes(db.Model):
  
    __tablename__ = "clientes"


    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    empresa = db.Column(db.String(120), nullable=False)
    celular = db.Column(db.String(50), nullable=False)
    mensaje = db.Column(db.String(500), nullable=False)
    checkbox = db.Column(db.Boolean, nullable=False)
    cotizaciones = db.relationship('Cotizacion', backref='clientes_cotizan', lazy=True)
    solicitudes = db.relationship('Solicitud', backref='sol_client', lazy=True)

    
    

    def __init__(self, nombres, apellidos, correo, empresa, celular, mensaje, checkbox, sol_client):
        
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.empresa = empresa
        self.celular = celular
        self.mensaje = mensaje
        self.checkbox = checkbox
        self.sol_client = sol_client
        
        
    

    def __repr__(self):
        return '<Clientes %r>' % self.id


class Solicitud(db.Model):
    __tablename__ = "solicitud"

    id = db.Column(db.Integer, primary_key=True)
    
    servicio_campo = db.Column(db.String(120), nullable=False)
    asesore = db.Column(db.String(120), nullable=False)

     # LLAVE FORANEA
    solicitud_cliente = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=True)
    solicitudes_cliente = db.relationship('Cotizacion', backref='clientes_solicitan', lazy=True)

    

    def __init__(self, servicio_campo, asesore, sol_client):
       
        self.servicio_campo = servicio_campo
        self.asesore = asesore
        self.sol_client = sol_client
       



class Cotizacion(db.Model):
    __tablename__ = "cotizacion"

    id = db.Column(db.Integer, primary_key=True)
   
    numero_horas = db.Column(db.Integer, nullable=False)
    
    descuento = db.Column(db.Integer, nullable=False)

    # LLAVE FORANEA
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=True)
    solicitud_id = db.Column(db.Integer, db.ForeignKey("solicitud.id"), nullable=True)
    

    def __init__(self, numero_horas, descuento, clientes_cotizan, clientes_solicitan):
       
        self.numero_horas = numero_horas
        self.descuento = descuento
        self.clientes_cotizan = clientes_cotizan
        self.clientes_solicitan = clientes_solicitan
      
       

    def __repr__(self):
        return '<Cotizacion %r>' % self.id