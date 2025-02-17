def update_from_ref(self, LUT_ref):
    """Compute and set the parameter attributes of the EEC from a reference LUT:
    resistance, skin effect factors, inductance, fluxlinkage and back emf

    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    LUT_ref : LUTdq
        a LUTdq object

    """

    if self.type_skin_effect:
        # Update skin effect
        self.comp_skin_effect()

    eec_ref = LUT_ref.get_eec()
    Tsta_ref, Trot_ref = eec_ref.Tsta, eec_ref.Trot
    Xkr_skinS_ref, Xke_skinS_ref = eec_ref.Xkr_skinS, eec_ref.Xke_skinS
    Xkr_skinR_ref, Xke_skinR_ref = eec_ref.Xkr_skinR, eec_ref.Xke_skinS

    # Update stator winding resistance
    if eec_ref.R1 is None:
        self.comp_R1()
    else:
        self.comp_R1(R1_ref=eec_ref.R1 / Xkr_skinS_ref, T_ref=Tsta_ref)

    # Update stator winding flux in open-circuit
    Phi_dqh_mag = LUT_ref.get_Phi_dqh_mag_mean()
    self.Phid = Phi_dqh_mag[0]
    self.Phiq = Phi_dqh_mag[1]

    # Compute stator winding flux
    Phi_dqh = LUT_ref.interp_Phi_dqh(
        Id=self.OP.get_Id_Iq()["Id"], Iq=self.OP.get_Id_Iq()["Iq"]
    )
    self.Phid = Phi_dqh[0]
    self.Phiq = Phi_dqh[1]

    # Compute stator winding inductance
    Ldqh = LUT_ref.get_L_dqh(
        Id=self.OP.get_Id_Iq()["Id"], Iq=self.OP.get_Id_Iq()["Iq"], Phi_dqh=Phi_dqh
    )
    self.Ld = Ldqh[0]
    self.Lq = Ldqh[1]
