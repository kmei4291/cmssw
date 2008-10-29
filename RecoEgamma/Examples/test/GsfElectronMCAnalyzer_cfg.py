import FWCore.ParameterSet.Config as cms

process = cms.Process("readelectrons")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
       '/store/relval/CMSSW_2_1_7/RelValSingleElectronPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0001/6AC34254-A77D-DD11-A69E-000423D99B3E.root',
       '/store/relval/CMSSW_2_1_7/RelValSingleElectronPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0001/CEF2036E-A77D-DD11-8C3E-001617DBD556.root',
       '/store/relval/CMSSW_2_1_7/RelValSingleElectronPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0001/DA54377C-A77D-DD11-B415-000423D98C20.root',
       '/store/relval/CMSSW_2_1_7/RelValSingleElectronPt10/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/F6AD9822-437E-DD11-8D4C-001617DBD332.root'
    )
)

process.PoolSource.fileNames = [
       '/store/relval/CMSSW_2_1_8/RelValSingleElectronPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/26127B91-5E82-DD11-ACA1-000423D95220.root',
       '/store/relval/CMSSW_2_1_8/RelValSingleElectronPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/5289417D-5E82-DD11-9911-001617C3B76E.root',
       '/store/relval/CMSSW_2_1_8/RelValSingleElectronPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/74716D79-5E82-DD11-B6D5-001617DBD224.root',
       '/store/relval/CMSSW_2_1_8/RelValSingleElectronPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0002/9C35CE9A-5E82-DD11-BC6A-001617E30D40.root',
       '/store/relval/CMSSW_2_1_8/RelValSingleElectronPt35/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/IDEAL_V9_v1/0003/AE85EEF7-A682-DD11-8C83-000423D992A4.root'
       ]

process.gsfElectronAnalysis = cms.EDAnalyzer("GsfElectronMCAnalyzer",
    electronCollection = cms.InputTag("pixelMatchGsfElectrons"),
    mcTruthCollection = cms.InputTag("source"),
    outputFile = cms.string('gsfElectronHistos_mc.root'),
    MaxPt = cms.double(100.0),
    DeltaR = cms.double(0.05),
    MaxAbsEta = cms.double(2.5),
    Etamin = cms.double(-2.5),
    Etamax = cms.double(2.5),
    Phimax = cms.double(3.2),
    Phimin = cms.double(-3.2),
    Ptmax = cms.double(100.0),
    Pmax = cms.double(300.0),
    Eopmax = cms.double(5.0),
    Eopmaxsht = cms.double(3.0),
    Detamin = cms.double(-0.005),
    Detamax = cms.double(0.005),
    Dphimin = cms.double(-0.01),
    Dphimax = cms.double(0.01),
    Dphimatchmin = cms.double(-0.2),
    Dphimatchmax = cms.double(0.2),
    Detamatchmin = cms.double(-0.05),
    Detamatchmax = cms.double(0.05),
    Fhitsmax = cms.double(20.0),
    Lhitsmax = cms.double(10.0),
    Nbinxyz = cms.int32(50),
    Nbineop2D = cms.int32(30),
    Nbinp = cms.int32(50),
    Nbineta2D = cms.int32(50),
    Nbinfhits = cms.int32(20),
    Nbinlhits = cms.int32(5),
    Nbinpteff = cms.int32(19),
    Nbinphi2D = cms.int32(32),
    Nbindetamatch2D = cms.int32(50),
    Nbineta = cms.int32(50),
    Nbinp2D = cms.int32(50),
    Nbindeta = cms.int32(100),
    Nbinpt2D = cms.int32(50),
    Nbindetamatch = cms.int32(100),
    Nbinphi = cms.int32(64),
    Nbindphimatch = cms.int32(100),
    Nbinpt = cms.int32(50),
    Nbindphimatch2D = cms.int32(50),
    Nbindphi = cms.int32(100),
    Nbineop = cms.int32(50)
)

process.p = cms.Path(process.gsfElectronAnalysis)


