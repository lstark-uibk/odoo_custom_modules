from  odoo import http
from odoo.http import request


class InputForm(http.Controller):
    @http.route('/ProduzentInnenformular',website = True, auth='public')
    def input_form(self,**kw):
        # pass
        # return "This is the input form in making"
        # return  request.render("inputform_prod_cons.create_prod",{})
        return  request.render("inputform_prod_cons.produzentInnenformular",{})
    # @http.route('/OldProduzentInnenformular',website = True, auth='public')
    # def input_form(self,**kw):
    #     # pass
    #     # return "This is the input form in making"
    #     # return  request.render("inputform_prod_cons.create_prod",{})
    #     return  request.render("inputform_prod_cons.create_prod",{})

    #this is what happens when the submit button is pushed

    @http.route('/DankefuersEintragen',website=True)
    def create_new_input(self,**kw):
        print("YEAH created",kw)
        dict_of_entries = kw
        dict_of_entries["name"] = f"{dict_of_entries['firstname']} {dict_of_entries['surename']}"
        new_record = request.env['res.partner'].sudo().create(kw)
        # new_record.action_send_mail()
        # return http.request.render("Konsumenten_Produzenten_app.prod_thanks",{})