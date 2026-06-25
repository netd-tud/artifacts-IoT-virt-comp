var SCALE_FACTOR = 1;

var BITLIST = []

var ACTIVE_KINDERSICHERUNG_CTRL_IDX = 10;
var ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX = 11;
var ACTIVE_KINDERSICHERUNG_CTRL_OLD_IDX = 12;
var ACTIVE_FH_TUERMODUL_CTRL_IDX = 13;
var ACTIVE_FH_TUERMODUL_CTRL_COPY_IDX = 14;
var ACTIVE_FH_TUERMODUL_CTRL_OLD_IDX = 15;
var ACTIVE_EINKLEMMSCHUTZ_CTRL_IDX = 16;
var ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX = 17;
var ACTIVE_EINKLEMMSCHUTZ_CTRL_OLD_IDX = 18;
var ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX = 19;
var ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX = 20;
var ACTIVE_BLOCK_ERKENNUNG_CTRL_OLD_IDX = 21;
var ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX = 0;
var ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_COPY_IDX = 1;
var TM_ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLCH_BLOCK_ERKENNUNG_CTRL__N_COPY = 0;
var ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX = 4;
var ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX = 5;
var EXITED_BEREIT_FH_TUERMODUL_CTRL_IDX = 6;
var EXITED_BEREIT_FH_TUERMODUL_CTRL_COPY_IDX = 7;
var TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL = 0;
var TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = 0;
var SC_FH_TUERMODUL_CTRL_2375_2 = 0;
var SC_FH_TUERMODUL_CTRL_2352_1 = 0;
var SC_FH_TUERMODUL_CTRL_2329_1 = 0;
var FH_TUERMODUL_CTRL__N = 0;
var FH_TUERMODUL_CTRL__N_COPY = 0;
var FH_TUERMODUL_CTRL__N_OLD = 0;
var SC_FH_TUERMODUL_CTRL_1781_10 = 0;
var SC_FH_TUERMODUL_CTRL_1739_10 = 0;
var FH_TUERMODUL__POSITION = 0;
var FH_TUERMODUL__I_EIN = 0;
var FH_TUERMODUL__I_EIN_OLD = 0;
var FH_DU__MFH = 0;
var FH_DU__MFH_COPY = 0;
var FH_DU__POSITION = 0;
var FH_DU__I_EIN = 0;
var FH_DU__I_EIN_OLD = 0;
var BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 0;
var BLOCK_ERKENNUNG_CTRL__I_EIN_MAX_COPY = 0;
var BLOCK_ERKENNUNG_CTRL__N = 0;
var BLOCK_ERKENNUNG_CTRL__N_COPY = 0;
var BLOCK_ERKENNUNG_CTRL__N_OLD = 0;
var FH_TUERMODUL_CTRL__INREVERS2 = 0;
var FH_TUERMODUL_CTRL__INREVERS2_COPY = 0;
var FH_TUERMODUL_CTRL__INREVERS1 = 0;
var FH_TUERMODUL_CTRL__INREVERS1_COPY = 0;
var FH_TUERMODUL_CTRL__FT = 0;
var FH_TUERMODUL__SFHZ_ZENTRAL = 0;
var FH_TUERMODUL__SFHZ_ZENTRAL_OLD = 0;
var FH_TUERMODUL__SFHZ_MEC = 0;
var FH_TUERMODUL__SFHZ_MEC_OLD = 0;
var FH_TUERMODUL__SFHA_ZENTRAL = 0;
var FH_TUERMODUL__SFHA_ZENTRAL_OLD = 0;
var FH_TUERMODUL__SFHA_MEC = 0;
var FH_TUERMODUL__SFHA_MEC_OLD = 0;
var FH_TUERMODUL__KL_50 = 0;
var FH_TUERMODUL__BLOCK = 0;
var FH_TUERMODUL__BLOCK_COPY = 0;
var FH_TUERMODUL__BLOCK_OLD = 0;
var FH_TUERMODUL__FT = 0;
var FH_TUERMODUL__SFHZ = 0;
var FH_TUERMODUL__SFHZ_COPY = 0;
var FH_TUERMODUL__SFHZ_OLD = 0;
var FH_TUERMODUL__SFHA = 0;
var FH_TUERMODUL__SFHA_COPY = 0;
var FH_TUERMODUL__SFHA_OLD = 0;
var FH_TUERMODUL__MFHZ = 0;
var FH_TUERMODUL__MFHZ_COPY = 0;
var FH_TUERMODUL__MFHZ_OLD = 0;
var FH_TUERMODUL__MFHA = 0;
var FH_TUERMODUL__MFHA_COPY = 0;
var FH_TUERMODUL__MFHA_OLD = 0;
var FH_TUERMODUL__EKS_LEISTE_AKTIV = 0;
var FH_TUERMODUL__EKS_LEISTE_AKTIV_OLD = 0;
var FH_TUERMODUL__COM_OPEN = 0;
var FH_TUERMODUL__COM_CLOSE = 0;
var FH_DU__KL_50 = 0;
var FH_DU__S_FH_FTZU = 0;
var FH_DU__S_FH_FTAUF = 0;
var FH_DU__FT = 0;
var FH_DU__EKS_LEISTE_AKTIV = 0;
var FH_DU__EKS_LEISTE_AKTIV_OLD = 0;
var FH_DU__S_FH_TMBFAUFCAN = 0;
var FH_DU__S_FH_TMBFAUFCAN_COPY = 0;
var FH_DU__S_FH_TMBFAUFCAN_OLD = 0;
var FH_DU__S_FH_TMBFZUCAN = 0;
var FH_DU__S_FH_TMBFZUCAN_COPY = 0;
var FH_DU__S_FH_TMBFZUCAN_OLD = 0;
var FH_DU__S_FH_TMBFZUDISC = 0;
var FH_DU__S_FH_TMBFZUDISC_OLD = 0;
var FH_DU__S_FH_TMBFAUFDISC = 0;
var FH_DU__S_FH_TMBFAUFDISC_OLD = 0;
var FH_DU__S_FH_ZUDISC = 0;
var FH_DU__S_FH_AUFDISC = 0;
var FH_DU__DOOR_ID = 0;
var FH_DU__BLOCK = 0;
var FH_DU__BLOCK_COPY = 0;
var FH_DU__BLOCK_OLD = 0;
var FH_DU__MFHZ = 0;
var FH_DU__MFHZ_COPY = 0;
var FH_DU__MFHZ_OLD = 0;
var FH_DU__MFHA = 0;
var FH_DU__MFHA_COPY = 0;
var FH_DU__MFHA_OLD = 0;
var FH_TUERMODUL_CTRL__END_REVERS_IDX = 22;
var FH_TUERMODUL_CTRL__END_REVERS_COPY_IDX = 23;
var FH_TUERMODUL__EINKLEMMUNG_IDX = 24;

var TIME = 0;
var STABLE = 0;
var STEP = 0;

var NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 0;
var ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
var MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
var KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
var B_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var A_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
var FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 0;
var EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 0;
var BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 0;
var BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 0;

function interface() {
    if (BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] !== 0) {
        TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = TIME;
    }
    if (BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] !== 0 || BITLIST[EXITED_BEREIT_FH_TUERMODUL_CTRL_IDX] !== 0) {
        TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL = TIME;
    }
    if (SC_FH_TUERMODUL_CTRL_2375_2 !== 0 && TIME - SC_FH_TUERMODUL_CTRL_2375_2 >= 1) {
        FH_TUERMODUL__MFHA_COPY = 0;
        SC_FH_TUERMODUL_CTRL_2375_2 = 0;
    }
    if (SC_FH_TUERMODUL_CTRL_2352_1 !== 0 && TIME - SC_FH_TUERMODUL_CTRL_2352_1 >= 1) {
        FH_TUERMODUL__MFHZ_COPY = 0;
        SC_FH_TUERMODUL_CTRL_2352_1 = 0;
    }
    if (SC_FH_TUERMODUL_CTRL_2329_1 !== 0 && TIME - SC_FH_TUERMODUL_CTRL_2329_1 >= 1) {
        FH_TUERMODUL__MFHZ_COPY = 0;
        SC_FH_TUERMODUL_CTRL_2329_1 = 0;
    }
    if (SC_FH_TUERMODUL_CTRL_1781_10 !== 0 && TIME - SC_FH_TUERMODUL_CTRL_1781_10 >= 1) {
        SC_FH_TUERMODUL_CTRL_1781_10 = 0;
    }
    if (SC_FH_TUERMODUL_CTRL_1739_10 !== 0 && TIME - SC_FH_TUERMODUL_CTRL_1739_10 >= 1) {
        SC_FH_TUERMODUL_CTRL_1739_10 = 0;
    }
    if (BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] !== 0 || BLOCK_ERKENNUNG_CTRL__N !== BLOCK_ERKENNUNG_CTRL__N_OLD) {
        TM_ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLCH_BLOCK_ERKENNUNG_CTRL__N_COPY = TIME;
    }
}

function init() {
    TM_ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLCH_BLOCK_ERKENNUNG_CTRL__N_COPY = 0;
    TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL = 0;
    TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL = 0;
    NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 0;
    ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
    MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
    KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
    B_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    A_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
    FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 0;
    EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 0;
    BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 0;
    BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 0;
}

function generic_KINDERSICHERUNG_CTRL() {
    if (BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_IDX] !== 0) {
        if (KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE === 1) {
            if (! (FH_TUERMODUL__SFHA_ZENTRAL !== 0 || FH_TUERMODUL__SFHZ_ZENTRAL !== 0)) {
                STABLE = 0;
                FH_TUERMODUL__SFHZ_COPY = 0;
                FH_TUERMODUL__SFHA_COPY = 0;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 3;
                ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
            } else {
                if (ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE === 1) {
                    if (FH_TUERMODUL__SFHA_ZENTRAL !== 0 && ! (FH_TUERMODUL__SFHA_ZENTRAL_OLD !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHA_COPY = 1;

                        ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (FH_TUERMODUL__SFHZ_ZENTRAL !== 0 && ! (FH_TUERMODUL__SFHZ_ZENTRAL_OLD !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHZ_COPY = 1;

                        ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (! (FH_TUERMODUL__SFHA_ZENTRAL !== 0) && FH_TUERMODUL__SFHA_ZENTRAL_OLD !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHA_COPY = 0;

                        ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (! (FH_TUERMODUL__SFHZ_ZENTRAL !== 0) && FH_TUERMODUL__SFHZ_ZENTRAL_OLD !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHZ_COPY = 0;

                        ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    }
                } else {
                    STABLE = 0;
                }
            }
        } else if (KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE === 2) {
            if (! (FH_TUERMODUL__SFHA_MEC !== 0 || FH_TUERMODUL__SFHZ_MEC !== 0)) {
                STABLE = 0;
                FH_TUERMODUL__SFHZ_COPY = 0;
                FH_TUERMODUL__SFHA_COPY = 0;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 3;
                MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 0;
            } else {
                if (MEC_KINDERSICHERUNG_CTRL_NEXT_STATE === 1) {
                    if (FH_TUERMODUL__SFHA_MEC !== 0 && ! (FH_TUERMODUL__SFHA_MEC_OLD !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHA_COPY = 1;

                        MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (FH_TUERMODUL__SFHZ_MEC !== 0 && ! (FH_TUERMODUL__SFHZ_MEC_OLD !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHZ_COPY = 1;

                        MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (! (FH_TUERMODUL__SFHA_MEC !== 0) && FH_TUERMODUL__SFHA_MEC_OLD !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHA_COPY = 0;

                        MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    } else if (! (FH_TUERMODUL__SFHZ_MEC !== 0) && FH_TUERMODUL__SFHZ_MEC_OLD !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__SFHZ_COPY = 0;

                        MEC_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
                    }
                } else {
                    STABLE = 0;
                }
            }
        } else if (KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE === 3) {
            if (! (FH_TUERMODUL__KL_50 !== 0) && (FH_TUERMODUL__SFHZ_MEC !== 0 && FH_TUERMODUL__SFHA_MEC !== 0)) {
                STABLE = 0;
                FH_TUERMODUL__SFHZ_COPY = 1;
                FH_TUERMODUL__SFHA_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 2;
            } else if (! (FH_TUERMODUL__KL_50 !== 0) && (FH_TUERMODUL__SFHZ_MEC !== 0 && FH_TUERMODUL__SFHA_MEC === 0)) {
                STABLE = 0;
                FH_TUERMODUL__SFHZ_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 2;
            } else if (! (FH_TUERMODUL__KL_50 !== 0) && (FH_TUERMODUL__SFHZ_MEC === 0 && FH_TUERMODUL__SFHA_MEC !== 0)) {
                STABLE = 0;
                FH_TUERMODUL__SFHA_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 2;
            } else if (FH_TUERMODUL__SFHZ_ZENTRAL === 0 && FH_TUERMODUL__SFHA_ZENTRAL !== 0 && FH_TUERMODUL__KL_50 === 0) {
                STABLE = 0;
                FH_TUERMODUL__SFHA_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
            } else if (FH_TUERMODUL__SFHZ_ZENTRAL !== 0 && FH_TUERMODUL__SFHA_ZENTRAL !== 0) {
                STABLE = 0;
                FH_TUERMODUL__SFHA_COPY = 1;
                FH_TUERMODUL__SFHZ_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
            } else if (FH_TUERMODUL__SFHZ_ZENTRAL !== 0 && FH_TUERMODUL__SFHA_ZENTRAL === 0 && FH_TUERMODUL__KL_50 === 0) {
                STABLE = 0;
                FH_TUERMODUL__SFHZ_COPY = 1;

                KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 1;
        } else {
            STABLE = 0;
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 3;
        }
    }
  }
}

function generic_FH_TUERMODUL_CTRL() {
    if (! (BITLIST[ACTIVE_FH_TUERMODUL_CTRL_IDX] !== 0) && BITLIST[ACTIVE_FH_TUERMODUL_CTRL_OLD_IDX] !== 0 && ! (BITLIST[ACTIVE_FH_TUERMODUL_CTRL_COPY_IDX] !== 0)) {
        BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] = 0;
        BITLIST[EXITED_BEREIT_FH_TUERMODUL_CTRL_IDX] = 0;
    }
    if (BITLIST[ACTIVE_FH_TUERMODUL_CTRL_IDX] !== 0) {
        if (BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_IDX] === 0) {
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 3;
        }
        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX] = 0;
        if (BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX] === 0) {
            BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0;
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
        }
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] = 0;
        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX] = 1;
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] = 1;
        if (B_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
            if (FH_TUERMODUL_CTRL__N === 59 && ! (FH_TUERMODUL_CTRL__N_OLD === 59)) {
                STABLE = 0;

                B_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
            }
        } else if (B_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
            if (((FH_TUERMODUL__BLOCK !== 0 && !(FH_TUERMODUL__BLOCK_OLD !== 0))) && ((FH_TUERMODUL__MFHZ !== 0))) {
                STABLE = 0;
                FH_TUERMODUL__MFHZ_COPY = 0;
                SC_FH_TUERMODUL_CTRL_2329_1 = TIME;

                B_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
            } else {
                if (NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE === 1) {
                    if (! (FH_TUERMODUL__SFHZ !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHZ_COPY = 0;

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 3;
                    }
                } else if (NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE === 2) {
                    if (! (FH_TUERMODUL__SFHA !== 0)) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHA_COPY = 0;

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 3;
                    }
                } else if (NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE === 3) {
                    if (FH_TUERMODUL__SFHA !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHA_COPY = 1;

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 2;
                    } else if (FH_TUERMODUL__SFHZ !== 0) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHZ_COPY = 1;

                        NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 1;
                    }
                } else {
                    STABLE = 0;
                    NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 3;
                }
            }
        } else if (B_FH_TUERMODUL_CTRL_NEXT_STATE === 3) {
            if (((FH_TUERMODUL_CTRL__N > 60 && ! (FH_TUERMODUL_CTRL__N_OLD > 60))) && ((! (FH_TUERMODUL_CTRL__INREVERS1 !== 0 || FH_TUERMODUL_CTRL__INREVERS2 !== 0)))) {
                STABLE = 0;
                FH_TUERMODUL__MFHZ_COPY = 0;
                FH_TUERMODUL__MFHA_COPY = 0;

                B_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
            } else if (((FH_TUERMODUL__BLOCK !== 0 && ! (FH_TUERMODUL__BLOCK_OLD !== 0))) && ((FH_TUERMODUL__MFHA !== 0))) {
                STABLE = 0;
                FH_TUERMODUL__MFHA_COPY = 0;
                SC_FH_TUERMODUL_CTRL_2375_2 = TIME;

                B_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 3;
            } else if (((FH_TUERMODUL__BLOCK !== 0 && ! (FH_TUERMODUL__BLOCK_OLD !== 0))) && ((FH_TUERMODUL__MFHZ !== 0))) {
                STABLE = 0;
                FH_TUERMODUL__MFHZ_COPY = 0;
                SC_FH_TUERMODUL_CTRL_2352_1 = TIME;

                B_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE = 3;
            } else {
                if (INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                    if (FH_TUERMODUL__POSITION >= 405) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHA_COPY = 0;

                        INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                    } else {
                        if (OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                            if ((FH_TUERMODUL__SFHZ !== 0 && ! (FH_TUERMODUL__SFHZ_OLD !== 0)) || (FH_TUERMODUL__SFHA !== 0 && ! (FH_TUERMODUL__SFHA_OLD !== 0))) {
                                STABLE = 0;
                                FH_TUERMODUL__MFHA_COPY = 0;

                                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                                OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
                            }
                        } else if (OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
                            if (FH_TUERMODUL__SFHZ !== 0 && ! (FH_TUERMODUL__SFHZ_OLD !== 0)) {
                                STABLE = 0;

                                OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                            } else if (! (FH_TUERMODUL__SFHA !== 0) && FH_TUERMODUL__SFHA_OLD !== 0) {
                                STABLE = 0;
                                FH_TUERMODUL__MFHA_COPY = 0;

                                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                                OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
                            }
                        } else {
                            STABLE = 0;
                            OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                        }
                    }
                } else if (INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
                    if (FH_TUERMODUL__POSITION <= 0) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHZ_COPY = 0;

                        INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                    } else {
                        if (SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                            if ((FH_TUERMODUL__SFHA !== 0 && ! (FH_TUERMODUL__SFHA_OLD !== 0)) || (FH_TUERMODUL__SFHZ !== 0 && ! (FH_TUERMODUL__SFHZ_OLD !== 0))) {
                                STABLE = 0;
                                FH_TUERMODUL__MFHZ_COPY = 0;

                                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                            } else {
                                if (TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                                    BITLIST[FH_TUERMODUL_CTRL__END_REVERS_COPY_IDX] = 0;
                                    if (BITLIST[FH_TUERMODUL_CTRL__END_REVERS_IDX] !== 0) {
                                        STABLE = 0;
                                        FH_TUERMODUL__MFHZ_COPY = 1;
                                        FH_TUERMODUL_CTRL__INREVERS2_COPY = 0;

                                        TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                                        FH_TUERMODUL__MFHA_COPY = 0;

                                        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                                    }
                                } else if (TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
                                    if (BITLIST[FH_TUERMODUL__EINKLEMMUNG_IDX] !== 0) {
                                        STABLE = 0;
                                        FH_TUERMODUL_CTRL__INREVERS2_COPY = 1;

                                        BITLIST[FH_TUERMODUL_CTRL__END_REVERS_COPY_IDX] = 1;
                                        TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                                        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 0;
                                        FH_TUERMODUL__MFHZ_COPY = 0;

                                        SC_FH_TUERMODUL_CTRL_1781_10 = TIME;
                                        FH_TUERMODUL__MFHA_COPY = 1;
                                    }
                                } else {
                                    STABLE = 0;
                                    TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                                    BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                                }
                            }
                        } else if (SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
                            if (! (FH_TUERMODUL__SFHZ !== 0) && FH_TUERMODUL__SFHZ_OLD !== 0) {
                                STABLE = 0;
                                FH_TUERMODUL__MFHZ_COPY = 0;

                                INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                            } else {
                                if (MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                                    BITLIST[FH_TUERMODUL_CTRL__END_REVERS_COPY_IDX] = 0;
                                    if (BITLIST[FH_TUERMODUL_CTRL__END_REVERS_IDX] !== 0) {
                                        STABLE = 0;
                                        FH_TUERMODUL_CTRL__INREVERS1_COPY = 0;

                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                                        FH_TUERMODUL__MFHA_COPY = 0;

                                        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                                        FH_TUERMODUL__MFHZ_COPY = 1;
                                    }
                                } else if (MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE === 2) {
                                    if (BITLIST[FH_TUERMODUL__EINKLEMMUNG_IDX] !== 0) {
                                        STABLE = 0;
                                        FH_TUERMODUL__MFHZ_COPY = 0;
                                        FH_TUERMODUL_CTRL__INREVERS1_COPY = 1;

                                        BITLIST[FH_TUERMODUL_CTRL__END_REVERS_COPY_IDX] = 1;
                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                                        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 0;

                                        SC_FH_TUERMODUL_CTRL_1739_10 = TIME;
                                        FH_TUERMODUL__MFHA_COPY = 1;
                                    } else if (FH_TUERMODUL__SFHA !== 0 && ! (FH_TUERMODUL__SFHA_OLD !== 0)) {
                                        STABLE = 0;

                                        SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 0;
                                    }
                                } else {
                                    STABLE = 0;
                                    MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                                    BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                                    FH_TUERMODUL__MFHZ_COPY = 1;
                                }
                            }
                        } else {
                            STABLE = 0;
                            SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                            MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                            BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                            FH_TUERMODUL__MFHZ_COPY = 1;
                        }
                    }
                } else if (INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE === 3) {
                    if (((FH_TUERMODUL__SFHZ !== 0 && ! (FH_TUERMODUL__SFHZ_OLD !== 0))) && ((FH_TUERMODUL__POSITION > 0))) {
                        STABLE = 0;

                        INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                        SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                        MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
                        FH_TUERMODUL__MFHZ_COPY = 1;
                    } else if (((FH_TUERMODUL__SFHA !== 0 && ! (FH_TUERMODUL__SFHA_OLD !== 0))) && ((FH_TUERMODUL__POSITION < 405))) {
                        STABLE = 0;
                        FH_TUERMODUL__MFHA_COPY = 1;

                        INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                        OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
                    }
                } else {
                    STABLE = 0;
                    INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE = 3;
                }
            }
        } else {
            STABLE = 0;
            B_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
        }

        if (A_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
            BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = 0;
            if ((STEP === 1 && TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL !== 0 && (TIME - TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL === 1)) && ((FH_TUERMODUL__MFHZ !== 0 || FH_TUERMODUL__MFHA !== 0))) {
                STABLE = 0;
                FH_TUERMODUL_CTRL__N = FH_TUERMODUL_CTRL__N + 1;

                A_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = 1;
                WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
            } else {
                if (WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE === 1) {
                    if ((STEP === 1 && TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL !== 0 && (TIME - TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL === 3)) && (((! (FH_TUERMODUL__MFHZ !== 0 || FH_TUERMODUL__MFHA !== 0)) && FH_TUERMODUL_CTRL__N > 0))) {
                        STABLE = 0;
                        FH_TUERMODUL_CTRL__N = FH_TUERMODUL_CTRL__N - 1;

                        WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                    }
                } else {
                    STABLE = 0;
                    BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = 1;
                    WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
                }
            }
        } else {
            STABLE = 0;
            FH_TUERMODUL_CTRL__N = 0;
            A_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
            BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = 1;
            WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
        }

        BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX];
        BITLIST[EXITED_BEREIT_FH_TUERMODUL_CTRL_COPY_IDX] = BITLIST[EXITED_BEREIT_FH_TUERMODUL_CTRL_IDX];
      }
    }

function generic_EINKLEMMSCHUTZ_CTRL() {
    if (BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_IDX] !== 0) {
        if (EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE === 1) {
            if (((FH_TUERMODUL__EKS_LEISTE_AKTIV !== 0 && ! (FH_TUERMODUL__EKS_LEISTE_AKTIV_OLD !== 0))) && ((! (FH_TUERMODUL__SFHZ !== 0 && FH_TUERMODUL__SFHA !== 0)))) {
                STABLE = 0;

                BITLIST[FH_TUERMODUL__EINKLEMMUNG_IDX] = 1;
                EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 2;
            }
        } else if (EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE === 2) {
            BITLIST[FH_TUERMODUL__EINKLEMMUNG_IDX] = 0;
            if (! (FH_TUERMODUL__EKS_LEISTE_AKTIV !== 0) && FH_TUERMODUL__EKS_LEISTE_AKTIV_OLD !== 0) {
                STABLE = 0;

                EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 1;
            }
        } else {
            STABLE = 0;
            EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 1;
        }
    }
  }

function generic_BLOCK_ERKENNUNG_CTRL() {
    if (! (BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX] !== 0) && BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_OLD_IDX] !== 0 && ! (BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] !== 0)) {
        BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0;
    }
    if ((BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX]) !== 0) {
        if (BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 1) {
            if ((FH_TUERMODUL__I_EIN !== FH_TUERMODUL__I_EIN_OLD) && ((FH_TUERMODUL__I_EIN > 0))) {
                STABLE = 0;
                FH_TUERMODUL__BLOCK_COPY = 0;

                BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 2;
                BLOCK_ERKENNUNG_CTRL__N = 0;
                BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 2;
                BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 3;
                BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 1;
            }
        } else if (BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 2) {
            if ((!(FH_TUERMODUL__MFHA !== 0) && FH_TUERMODUL__MFHA_OLD !== 0) || (! (FH_TUERMODUL__MFHZ !== 0) && FH_TUERMODUL__MFHZ_OLD !== 0)) {
                STABLE = 0;

                BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
                BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 0;
            } else {
                if (BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 1) {
                  BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
                } else if (BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 2) {
                    if (FH_TUERMODUL__I_EIN > (BLOCK_ERKENNUNG_CTRL__I_EIN_MAX - 2)) {
                        STABLE = 0;
                        FH_TUERMODUL__BLOCK_COPY = 1;

                        BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
                    }
                } else if (BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 3) {
                    BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0;
                    if (BLOCK_ERKENNUNG_CTRL__N === 11 && ! (BLOCK_ERKENNUNG_CTRL__N_OLD === 11)) {
                        STABLE = 0;

                        BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 2;
                    } else if (BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE === 3) {
                        if (STEP === 1 && TM_ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLCH_BLOCK_ERKENNUNG_CTRL__N_COPY !== 0 && false) {
                            BLOCK_ERKENNUNG_CTRL__N = BLOCK_ERKENNUNG_CTRL__N + 1;
                            if (FH_TUERMODUL__I_EIN > BLOCK_ERKENNUNG_CTRL__I_EIN_MAX) {
                                BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = FH_TUERMODUL__I_EIN;
                            }
                        }
                    }
                } else {
                    STABLE = 0;
                    BLOCK_ERKENNUNG_CTRL__N = 0;
                    BLOCK_ERKENNUNG_CTRL__I_EIN_MAX = 2;
                    BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 3;
                    BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 1;
                }
            }
        } else {
            STABLE = 0;
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
        }
    }
  }

function FH_DU() {
    TIME = 1;
    STABLE = 0;
    STEP = 0;
    while (STABLE === 0) {
        STABLE = 1;
        STEP = STEP + 1;
        if (FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE === 1) {
            if (! (FH_DU__MFHZ !== 0) && FH_DU__MFHZ_OLD !== 0) {
                STABLE = 0;
                FH_DU__MFH = 0;

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 2;
            }
        } else if (FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE === 2) {
            if (FH_DU__MFHZ !== 0 && ! (FH_DU__MFHZ_OLD !== 0)) {
                STABLE = 0;
                FH_DU__MFH = -100;

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 1;
            } else if (FH_DU__MFHA !== 0 && ! (FH_DU__MFHA_OLD !== 0)) {
                STABLE = 0;
                FH_DU__MFH = 100;

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 3;
            }
        } else if (FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE === 3) {
            if (! (FH_DU__MFHA !== 0) && FH_DU__MFHA_OLD !== 0) {
                STABLE = 0;
                FH_DU__MFH = 0;

                FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 2;
            }
        } else {
            STABLE = 0;
            FH_DU__MFH = 0;
            FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE = 2;
        }
        if (BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_IDX] === 0) {
            KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE = 3;
        }
        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX] = 0;
        if (BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_IDX] === 0) {
            EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE = 1;
        }
        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 0;
        if (BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX] === 0) {
            BITLIST[ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRL_IDX] = 0;
            BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE = 1;
        }
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] = 0;
        if (BITLIST[ACTIVE_FH_TUERMODUL_CTRL_IDX] === 0) {
            BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_IDX] = 0;
            BITLIST[EXITED_BEREIT_FH_TUERMODUL_CTRL_IDX] = 0;
            B_FH_TUERMODUL_CTRL_NEXT_STATE = 2;
            FH_TUERMODUL_CTRL__N = 0;
            A_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
            BITLIST[ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_COPY_IDX] = 1;
            WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE = 1;
        }
        BITLIST[ACTIVE_FH_TUERMODUL_CTRL_COPY_IDX] = 0;
        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX] = 1;
        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = 1;
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] = 1;
        BITLIST[ACTIVE_FH_TUERMODUL_CTRL_COPY_IDX] = 1;

        if (FH_DU__S_FH_TMBFZUCAN !== FH_DU__S_FH_TMBFZUCAN_OLD) {
            if (FH_DU__DOOR_ID !== 0) {
                FH_DU__S_FH_FTZU = FH_DU__S_FH_TMBFZUCAN;
            }
        }
        if (FH_DU__S_FH_TMBFZUDISC !== FH_DU__S_FH_TMBFZUDISC_OLD) {
            if (FH_DU__DOOR_ID === 0) {
                FH_DU__S_FH_TMBFZUCAN = FH_DU__S_FH_TMBFZUDISC;
            }
        }
        if (FH_DU__S_FH_TMBFAUFCAN !== FH_DU__S_FH_TMBFAUFCAN_OLD) {
            if (FH_DU__DOOR_ID !== 0) {
                FH_DU__S_FH_FTAUF = FH_DU__S_FH_TMBFAUFCAN;
            }
        }
        if (FH_DU__S_FH_TMBFAUFDISC !== FH_DU__S_FH_TMBFAUFDISC_OLD) {
            if (FH_DU__DOOR_ID === 0) {
                FH_DU__S_FH_TMBFAUFCAN = FH_DU__S_FH_TMBFAUFDISC;
            }
        }
        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_IDX] = BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_OLD_IDX];
        BITLIST[ACTIVE_FH_TUERMODUL_CTRL_IDX] = BITLIST[ACTIVE_FH_TUERMODUL_CTRL_OLD_IDX];
        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_IDX] = BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_OLD_IDX];
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX] = BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_OLD_IDX];
        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC;
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF;
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC;
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU;

        generic_KINDERSICHERUNG_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA;
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ;
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN;
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV;
        FH_DU__POSITION = FH_TUERMODUL__POSITION;
        FH_DU__FT = FH_TUERMODUL__FT;
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC;
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL;
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC;
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL;
        FH_DU__KL_50 = FH_TUERMODUL__KL_50;
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK;

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC;
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF;
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC;
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU;

        generic_FH_TUERMODUL_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA;
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ;
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN;
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV;
        FH_DU__POSITION = FH_TUERMODUL__POSITION;
        FH_DU__FT = FH_TUERMODUL__FT;
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC;
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL;
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC;
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL;
        FH_DU__KL_50 = FH_TUERMODUL__KL_50;
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK;

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC;
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF;
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC;
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU;

        generic_EINKLEMMSCHUTZ_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA;
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ;
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN;
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV;
        FH_DU__POSITION = FH_TUERMODUL__POSITION;
        FH_DU__FT = FH_TUERMODUL__FT;
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC;
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL;
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC;
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL;
        FH_DU__KL_50 = FH_TUERMODUL__KL_50;
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK;

        FH_TUERMODUL__SFHA_MEC = FH_DU__S_FH_AUFDISC;
        FH_TUERMODUL__SFHA_ZENTRAL = FH_DU__S_FH_FTAUF;
        FH_TUERMODUL__SFHZ_MEC = FH_DU__S_FH_ZUDISC;
        FH_TUERMODUL__SFHZ_ZENTRAL = FH_DU__S_FH_FTZU;

        generic_BLOCK_ERKENNUNG_CTRL()

        FH_DU__MFHA = FH_TUERMODUL__MFHA;
        FH_DU__MFHZ = FH_TUERMODUL__MFHZ;
        FH_DU__I_EIN = FH_TUERMODUL__I_EIN;
        FH_DU__EKS_LEISTE_AKTIV = FH_TUERMODUL__EKS_LEISTE_AKTIV;
        FH_DU__POSITION = FH_TUERMODUL__POSITION;
        FH_DU__FT = FH_TUERMODUL__FT;
        FH_DU__S_FH_AUFDISC = FH_TUERMODUL__SFHA_MEC;
        FH_DU__S_FH_FTAUF = FH_TUERMODUL__SFHA_ZENTRAL;
        FH_DU__S_FH_ZUDISC = FH_TUERMODUL__SFHZ_MEC;
        FH_DU__S_FH_FTZU = FH_TUERMODUL__SFHZ_ZENTRAL;
        FH_DU__KL_50 = FH_TUERMODUL__KL_50;
        FH_DU__BLOCK = FH_TUERMODUL__BLOCK;

        BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_COPY_IDX] = BITLIST[ACTIVE_KINDERSICHERUNG_CTRL_IDX];
        BITLIST[ACTIVE_FH_TUERMODUL_CTRL_COPY_IDX] = BITLIST[ACTIVE_FH_TUERMODUL_CTRL_IDX];
        BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_COPY_IDX] = BITLIST[ACTIVE_EINKLEMMSCHUTZ_CTRL_IDX];
        BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_COPY_IDX] = BITLIST[ACTIVE_BLOCK_ERKENNUNG_CTRL_IDX];
        FH_TUERMODUL_CTRL__N_OLD = FH_TUERMODUL_CTRL__N;
        FH_TUERMODUL__I_EIN_OLD = FH_TUERMODUL__I_EIN;
        FH_DU__MFH = FH_DU__MFH_COPY;
        FH_DU__I_EIN_OLD = FH_DU__I_EIN;
        BLOCK_ERKENNUNG_CTRL__N_OLD = BLOCK_ERKENNUNG_CTRL__N;
        FH_TUERMODUL__SFHZ_ZENTRAL_OLD = FH_TUERMODUL__SFHZ_ZENTRAL;
        FH_TUERMODUL__SFHZ_MEC_OLD = FH_TUERMODUL__SFHZ_MEC;
        FH_TUERMODUL__SFHA_ZENTRAL_OLD = FH_TUERMODUL__SFHA_ZENTRAL;
        FH_TUERMODUL__SFHA_MEC_OLD = FH_TUERMODUL__SFHA_MEC;
        FH_TUERMODUL__BLOCK = FH_TUERMODUL__BLOCK_COPY;
        FH_TUERMODUL__BLOCK_OLD = FH_TUERMODUL__BLOCK;
        FH_TUERMODUL__SFHZ = FH_TUERMODUL__SFHZ_COPY;
        FH_TUERMODUL__SFHZ_OLD = FH_TUERMODUL__SFHZ;
        FH_TUERMODUL__SFHA = FH_TUERMODUL__SFHA_COPY;
        FH_TUERMODUL__SFHA_OLD = FH_TUERMODUL__SFHA;
        FH_TUERMODUL__MFHZ = FH_TUERMODUL__MFHZ_COPY;
        FH_TUERMODUL__MFHZ_OLD = FH_TUERMODUL__MFHZ;
        FH_TUERMODUL__MFHA = FH_TUERMODUL__MFHA_COPY;
        FH_TUERMODUL__MFHA_OLD = FH_TUERMODUL__MFHA;
        FH_TUERMODUL__EKS_LEISTE_AKTIV_OLD = FH_TUERMODUL__EKS_LEISTE_AKTIV;
        FH_DU__EKS_LEISTE_AKTIV_OLD = FH_DU__EKS_LEISTE_AKTIV;
        FH_DU__S_FH_TMBFAUFCAN_OLD = FH_DU__S_FH_TMBFAUFCAN;
        FH_DU__S_FH_TMBFZUCAN_OLD = FH_DU__S_FH_TMBFZUCAN;
        FH_DU__S_FH_TMBFZUDISC_OLD = FH_DU__S_FH_TMBFZUDISC;
        FH_DU__S_FH_TMBFAUFDISC_OLD = FH_DU__S_FH_TMBFAUFDISC;
        FH_DU__BLOCK = FH_DU__BLOCK_COPY;
        FH_DU__BLOCK_OLD = FH_DU__BLOCK;
        FH_DU__MFHZ = FH_DU__MFHZ_COPY;
        FH_DU__MFHZ_OLD = FH_DU__MFHZ;
        FH_DU__MFHA = FH_DU__MFHA_COPY;
        FH_DU__MFHA_OLD = FH_DU__MFHA;
      }
    }

function initialise_benchmark() {
}

function benchmark_body(lsf) {
    for (var _ = 0; _ < lsf; _++) {;
            for (var i = 0; i < 64; i++) {;
              BITLIST[i] = 0;
            }
            init()

            interface()
            FH_DU()
    }
    return 0
  }

function verify_benchmark(unused) {
    var expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];;

    for(var i = 0; i < 64; i++) {;
        if (BITLIST[i] !== expected[i]) {
            return false;
        }
      }
    if (TM_ENTERED_EINSCHALTSTROM_MESSEN_BLOCK_ERKENNUNG_CTRLCH_BLOCK_ERKENNUNG_CTRL__N_COPY !== 0 || TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRLEXITED_BEREIT_FH_TUERMODUL_CTRL !== 0 || TM_ENTERED_WIEDERHOLSPERRE_FH_TUERMODUL_CTRL !== 0 || NICHT_INITIALISIERT_NICHT_INITIALISIERT_NEXT_STATE !== 0 || ZENTRAL_KINDERSICHERUNG_CTRL_NEXT_STATE !== 0 || MEC_KINDERSICHERUNG_CTRL_NEXT_STATE !== 0 || KINDERSICHERUNG_CTRL_KINDERSICHERUNG_CTRL_NEXT_STATE !== 3 || B_FH_TUERMODUL_CTRL_NEXT_STATE !== 2 || A_FH_TUERMODUL_CTRL_NEXT_STATE !== 1 || WIEDERHOLSPERRE_FH_TUERMODUL_CTRL_NEXT_STATE !== 1 || INITIALISIERT_FH_TUERMODUL_CTRL_NEXT_STATE !== 0 || TIPP_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE !== 0 || MANUELL_SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE !== 0 || OEFFNEN_FH_TUERMODUL_CTRL_NEXT_STATE !== 0 || SCHLIESSEN_FH_TUERMODUL_CTRL_NEXT_STATE !== 0 || FH_STEUERUNG_DUMMY_FH_STEUERUNG_DUMMY_NEXT_STATE !== 2 || EINKLEMMSCHUTZ_CTRL_EINKLEMMSCHUTZ_CTRL_NEXT_STATE !== 1 || BEWEGUNG_BLOCK_ERKENNUNG_CTRL_NEXT_STATE !== 0 || BLOCK_ERKENNUNG_CTRL_BLOCK_ERKENNUNG_CTRL_NEXT_STATE !== 1) {
      return false;
    }
    return true
  }

function benchmark() {
  initialise_benchmark()
  var res = benchmark_body(SCALE_FACTOR);
  return verify_benchmark(res)
}

benchmark();
