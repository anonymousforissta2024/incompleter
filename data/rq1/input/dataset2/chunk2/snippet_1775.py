#Source: https://stackoverflow.com/questions/72119681/attributeerror-could-not-locate-column-in-row-for-column-sa-instance-state-f
@app.route('/cotizaciones/crear/<int:id>', methods=("GET", "POST"))

@login_required

def crearcotizacion(id):
    
    
    datos_clientes = (db.session.query(Clientes.id, Clientes.nombres, Clientes.apellidos, Clientes.empresa, Clientes.correo, Solicitud.id, Solicitud.servicio_campo, Solicitud.asesore).join(Solicitud).filter_by(id=id).one())
    
    datos_solicitud = (db.session.query(Solicitud).filter_by(id=Solicitud.id).first())
    
    form = creacion_Cotizacion(request.form)

    if current_user.role == True:
        
        if request.method == 'POST':

            cotizan = Cotizacion(
           
            numero_horas=form.numero_horas.data,
            descuento=form.descuento.data,
            clientes_cotizan = datos_clientes,
            clientes_solicitan= datos_solicitud
            
            )
            
            db.session.add(cotizan)
            db.session.commit()
            flash('La cotización ha sido creado exitosamente', 'success')
            return render_template('crearcotizacion.html', form=form, id=id, datos_solicitud=datos_solicitud, datos_clientes=datos_clientes)
            
    else:
        abort(401)

    return render_template('crearcotizacion.html', nombres=current_user.nombres, correo=current_user.correo, role=current_user.role, id=id, form=form, datos_solicitud=datos_solicitud, datos_clientes=datos_clientes)