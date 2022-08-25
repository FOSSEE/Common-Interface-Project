def CLOCK_c(outroot, attribid, ordering):
    func_name = 'CLOCK_c'

    outnode = addNode(outroot, 'BasicBlock', blockType='h', **{'id': attribid},
        interfaceFunctionName=func_name, ordering=ordering, parent=1,
        simulationFunctionName='csuper', simulationFunctionType='DEFAULT', style=func_name)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'exprs'}, height=0, width=0)

    node = addNode(outnode, 'Array', **{'as': 'realParameters'},
        scilabClass='ScilabMList', varName='')

    innode = addDataNode(node, 'ScilabString', height=1, width=5)
    addDataData(innode, 'diagram')
    addDataData(innode, 'props')
    addDataData(innode, 'objs')
    addDataData(innode, 'version')
    addDataData(innode, 'contrib')

    innode = addNode(node, 'Array', scilabClass='ScilabTList')

    in2node = addDataNode(innode, 'ScilabString', height=1, width=11)
    addDataData(in2node, 'params')
    addDataData(in2node, 'wpar')
    addDataData(in2node, 'title')
    addDataData(in2node, 'tol')
    addDataData(in2node, 'tf')
    addDataData(in2node, 'context')
    addDataData(in2node, 'void1')
    addDataData(in2node, 'options')
    addDataData(in2node, 'void2')
    addDataData(in2node, 'void3')
    addDataData(in2node, 'doc')

    in2node = addDataNode(innode, 'ScilabDouble', height=1, width=6)
    addDataData(in2node, 600.0)
    addDataData(in2node, 450.0)
    addDataData(in2node, 0.0)
    addDataData(in2node, 0.0)
    addDataData(in2node, 600.0)
    addDataData(in2node, 450.0)

    in2node = addDataNode(innode, 'ScilabString', height=1, width=1)
    addDataData(in2node, 'Untitled')

    in2node = addDataNode(innode, 'ScilabDouble', height=7, width=1)
    addDataData(in2node, '1.0E-6', True)
    addDataData(in2node, '1.0E-6', True)
    addDataData(in2node, '1.0E-10', True)
    addDataData(in2node, 100001.0)
    addDataData(in2node, 0.0)
    addDataData(in2node, 1.0)
    addDataData(in2node, 0.0)

    in2node = addDataNode(innode, 'ScilabDouble', height=1, width=1)
    addDataData(in2node, 100000.0)

    in2node = addDataNode(innode, 'ScilabString', height=1, width=1)
    addDataData(in2node, '')

    in2node = addDataNode(innode, 'ScilabDouble', height=0, width=0)

    in2node = addNode(innode, 'Array', scilabClass='ScilabTList')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=6)
    addDataData(in3node, 'scsopt')
    addDataData(in3node, '3D')
    addDataData(in3node, 'Background')
    addDataData(in3node, 'Link')
    addDataData(in3node, 'ID')
    addDataData(in3node, 'Cmap')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=1)
    addDataData(in4node, 'true')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 33.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 8.0)
    addDataData(in3node, 1.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 1.0)
    addDataData(in3node, 5.0)

    in3node = addNode(in2node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 5.0)
    addDataData(in4node, 1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 4.0)
    addDataData(in4node, 1.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 0.8)
    addDataData(in3node, 0.8)
    addDataData(in3node, 0.8)

    in2node = addDataNode(innode, 'ScilabDouble', height=0, width=0)

    in2node = addDataNode(innode, 'ScilabDouble', height=0, width=0)

    in2node = addNode(innode, 'Array', scilabClass='ScilabList')

    innode = addNode(node, 'Array', scilabClass='ScilabList')

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=5)
    addDataData(in3node, 'Block')
    addDataData(in3node, 'graphics')
    addDataData(in3node, 'model')
    addDataData(in3node, 'gui')
    addDataData(in3node, 'doc')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=19)
    addDataData(in4node, 'graphics')
    addDataData(in4node, 'orig')
    addDataData(in4node, 'sz')
    addDataData(in4node, 'flip')
    addDataData(in4node, 'theta')
    addDataData(in4node, 'exprs')
    addDataData(in4node, 'pin')
    addDataData(in4node, 'pout')
    addDataData(in4node, 'pein')
    addDataData(in4node, 'peout')
    addDataData(in4node, 'gr_i')
    addDataData(in4node, 'id')
    addDataData(in4node, 'in_implicit')
    addDataData(in4node, 'out_implicit')
    addDataData(in4node, 'in_style')
    addDataData(in4node, 'out_style')
    addDataData(in4node, 'in_label')
    addDataData(in4node, 'out_label')
    addDataData(in4node, 'style')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 159.0)
    addDataData(in4node, -190.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 20.0)
    addDataData(in4node, 20.0)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=1)
    addDataData(in4node, 'true')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '1')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 5.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in5node = addDataNode(in4node, 'ScilabString', height=1, width=1)
    addDataData(in5node, 'xstringb(orig(1),orig(2),"CLKOUT_f",sz(1),sz(2));')

    in5node = addDataNode(in4node, 'ScilabDouble', height=1, width=1)
    addDataData(in5node, 8.0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'CLKOUT_f')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=24)
    addDataData(in4node, 'model')
    addDataData(in4node, 'sim')
    addDataData(in4node, 'in')
    addDataData(in4node, 'in2')
    addDataData(in4node, 'intyp')
    addDataData(in4node, 'out')
    addDataData(in4node, 'out2')
    addDataData(in4node, 'outtyp')
    addDataData(in4node, 'evtin')
    addDataData(in4node, 'evtout')
    addDataData(in4node, 'state')
    addDataData(in4node, 'dstate')
    addDataData(in4node, 'odstate')
    addDataData(in4node, 'rpar')
    addDataData(in4node, 'ipar')
    addDataData(in4node, 'opar')
    addDataData(in4node, 'blocktype')
    addDataData(in4node, 'firing')
    addDataData(in4node, 'dep_ut')
    addDataData(in4node, 'label')
    addDataData(in4node, 'nzcross')
    addDataData(in4node, 'nmode')
    addDataData(in4node, 'equations')
    addDataData(in4node, 'uid')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'output')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 1.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'd')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=2)
    addDataData(in4node, 'false')
    addDataData(in4node, 'false')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '103')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'CLKOUT_f')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '103')

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=5)
    addDataData(in3node, 'Block')
    addDataData(in3node, 'graphics')
    addDataData(in3node, 'model')
    addDataData(in3node, 'gui')
    addDataData(in3node, 'doc')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=19)
    addDataData(in4node, 'graphics')
    addDataData(in4node, 'orig')
    addDataData(in4node, 'sz')
    addDataData(in4node, 'flip')
    addDataData(in4node, 'theta')
    addDataData(in4node, 'exprs')
    addDataData(in4node, 'pin')
    addDataData(in4node, 'pout')
    addDataData(in4node, 'pein')
    addDataData(in4node, 'peout')
    addDataData(in4node, 'gr_i')
    addDataData(in4node, 'id')
    addDataData(in4node, 'in_implicit')
    addDataData(in4node, 'out_implicit')
    addDataData(in4node, 'in_style')
    addDataData(in4node, 'out_style')
    addDataData(in4node, 'in_label')
    addDataData(in4node, 'out_label')
    addDataData(in4node, 'style')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 0.0)
    addDataData(in4node, -40.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 40.0)
    addDataData(in4node, 40.0)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=1)
    addDataData(in4node, 'true')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabString', height=2, width=1)
    addDataData(in4node, '0.1')
    addDataData(in4node, '0.1')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 6.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 4.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in5node = addDataNode(in4node, 'ScilabString', height=1, width=1)
    addDataData(in5node, 'xstringb(orig(1),orig(2),"EVTDLY_c",sz(1),sz(2));')

    in5node = addDataNode(in4node, 'ScilabDouble', height=1, width=1)
    addDataData(in5node, 8.0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'EVTDLY_c')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=24)
    addDataData(in4node, 'model')
    addDataData(in4node, 'sim')
    addDataData(in4node, 'in')
    addDataData(in4node, 'in2')
    addDataData(in4node, 'intyp')
    addDataData(in4node, 'out')
    addDataData(in4node, 'out2')
    addDataData(in4node, 'outtyp')
    addDataData(in4node, 'evtin')
    addDataData(in4node, 'evtout')
    addDataData(in4node, 'state')
    addDataData(in4node, 'dstate')
    addDataData(in4node, 'odstate')
    addDataData(in4node, 'rpar')
    addDataData(in4node, 'ipar')
    addDataData(in4node, 'opar')
    addDataData(in4node, 'blocktype')
    addDataData(in4node, 'firing')
    addDataData(in4node, 'dep_ut')
    addDataData(in4node, 'label')
    addDataData(in4node, 'nzcross')
    addDataData(in4node, 'nmode')
    addDataData(in4node, 'equations')
    addDataData(in4node, 'uid')

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in5node = addDataNode(in4node, 'ScilabString', height=1, width=1)
    addDataData(in5node, 'evtdly4')

    in5node = addDataNode(in4node, 'ScilabDouble', height=1, width=1)
    addDataData(in5node, 4.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabDouble', height=2, width=1)
    addDataData(in4node, 0.1)
    addDataData(in4node, 0.1)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'd')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.1)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=2)
    addDataData(in4node, 'false')
    addDataData(in4node, 'false')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '104')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'EVTDLY_c')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '104')

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=5)
    addDataData(in3node, 'Block')
    addDataData(in3node, 'graphics')
    addDataData(in3node, 'model')
    addDataData(in3node, 'gui')
    addDataData(in3node, 'doc')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=19)
    addDataData(in4node, 'graphics')
    addDataData(in4node, 'orig')
    addDataData(in4node, 'sz')
    addDataData(in4node, 'flip')
    addDataData(in4node, 'theta')
    addDataData(in4node, 'exprs')
    addDataData(in4node, 'pin')
    addDataData(in4node, 'pout')
    addDataData(in4node, 'pein')
    addDataData(in4node, 'peout')
    addDataData(in4node, 'gr_i')
    addDataData(in4node, 'id')
    addDataData(in4node, 'in_implicit')
    addDataData(in4node, 'out_implicit')
    addDataData(in4node, 'in_style')
    addDataData(in4node, 'out_style')
    addDataData(in4node, 'in_label')
    addDataData(in4node, 'out_label')
    addDataData(in4node, 'style')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 189.3773266666667)
    addDataData(in4node, -235.33333333333331)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=2)
    addDataData(in4node, 7.0)
    addDataData(in4node, 7.0)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=1)
    addDataData(in4node, 'true')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 4.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=2, width=1)
    addDataData(in4node, 5.0)
    addDataData(in4node, 6.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in5node = addDataNode(in4node, 'ScilabString', height=1, width=1)
    addDataData(in5node, 'xstringb(orig(1),orig(2),"CLKSPLIT_f",sz(1),sz(2));')

    in5node = addDataNode(in4node, 'ScilabDouble', height=1, width=1)
    addDataData(in5node, 8.0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'CLKSPLIT_f')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabMList', varName='')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=24)
    addDataData(in4node, 'model')
    addDataData(in4node, 'sim')
    addDataData(in4node, 'in')
    addDataData(in4node, 'in2')
    addDataData(in4node, 'intyp')
    addDataData(in4node, 'out')
    addDataData(in4node, 'out2')
    addDataData(in4node, 'outtyp')
    addDataData(in4node, 'evtin')
    addDataData(in4node, 'evtout')
    addDataData(in4node, 'state')
    addDataData(in4node, 'dstate')
    addDataData(in4node, 'odstate')
    addDataData(in4node, 'rpar')
    addDataData(in4node, 'ipar')
    addDataData(in4node, 'opar')
    addDataData(in4node, 'blocktype')
    addDataData(in4node, 'firing')
    addDataData(in4node, 'dep_ut')
    addDataData(in4node, 'label')
    addDataData(in4node, 'nzcross')
    addDataData(in4node, 'nmode')
    addDataData(in4node, 'equations')
    addDataData(in4node, 'uid')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'split')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=2, width=1)
    addDataData(in4node, -1.0)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=0, width=0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, 'd')

    in4node = addDataNode(in3node, 'ScilabDouble', height=2, width=1)
    addDataData(in4node, -1.0)
    addDataData(in4node, -1.0)

    in4node = addDataNode(in3node, 'ScilabBoolean', height=1, width=2)
    addDataData(in4node, 'false')
    addDataData(in4node, 'false')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '')

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addDataNode(in3node, 'ScilabDouble', height=1, width=1)
    addDataData(in4node, 0.0)

    in4node = addNode(in3node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '105')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'CLKSPLIT_f')

    in3node = addNode(in2node, 'Array', scilabClass='ScilabList')

    in4node = addDataNode(in3node, 'ScilabString', height=1, width=1)
    addDataData(in4node, '105')

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=8)
    addDataData(in3node, 'Link')
    addDataData(in3node, 'xx')
    addDataData(in3node, 'yy')
    addDataData(in3node, 'id')
    addDataData(in3node, 'thick')
    addDataData(in3node, 'ct')
    addDataData(in3node, 'from')
    addDataData(in3node, 'to')

    in3node = addDataNode(in2node, 'ScilabDouble', height=3, width=1)
    addDataData(in3node, 60.0)
    addDataData(in3node, 180.0)
    addDataData(in3node, 199.8773266666667)

    in3node = addDataNode(in2node, 'ScilabDouble', height=3, width=1)
    addDataData(in3node, -44.0)
    addDataData(in3node, -260.0)
    addDataData(in3node, -224.33333333333331)

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'drawlink')

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 0.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 5.0)
    addDataData(in3node, -1.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 2.0)
    addDataData(in3node, 1.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 3.0)
    addDataData(in3node, 1.0)
    addDataData(in3node, 1.0)

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=8)
    addDataData(in3node, 'Link')
    addDataData(in3node, 'xx')
    addDataData(in3node, 'yy')
    addDataData(in3node, 'id')
    addDataData(in3node, 'thick')
    addDataData(in3node, 'ct')
    addDataData(in3node, 'from')
    addDataData(in3node, 'to')

    in3node = addDataNode(in2node, 'ScilabDouble', height=2, width=1)
    addDataData(in3node, 198.71066000000005)
    addDataData(in3node, 189.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=2, width=1)
    addDataData(in3node, -239.33333333333331)
    addDataData(in3node, -166.0)

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'drawlink')

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 0.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 5.0)
    addDataData(in3node, -1.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 3.0)
    addDataData(in3node, 1.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 1.0)
    addDataData(in3node, 1.0)
    addDataData(in3node, 1.0)

    in2node = addNode(innode, 'Array', scilabClass='ScilabMList', varName='')

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=8)
    addDataData(in3node, 'Link')
    addDataData(in3node, 'xx')
    addDataData(in3node, 'yy')
    addDataData(in3node, 'id')
    addDataData(in3node, 'thick')
    addDataData(in3node, 'ct')
    addDataData(in3node, 'from')
    addDataData(in3node, 'to')

    in3node = addDataNode(in2node, 'ScilabDouble', height=4, width=1)
    addDataData(in3node, 201.04399333333336)
    addDataData(in3node, 220.70999999999998)
    addDataData(in3node, 180.0)
    addDataData(in3node, 60.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=4, width=1)
    addDataData(in3node, -239.33333333333331)
    addDataData(in3node, -130.0)
    addDataData(in3node, -130.0)
    addDataData(in3node, 4.0)

    in3node = addDataNode(in2node, 'ScilabString', height=1, width=1)
    addDataData(in3node, 'drawlink')

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 0.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=2)
    addDataData(in3node, 5.0)
    addDataData(in3node, -1.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 3.0)
    addDataData(in3node, 2.0)
    addDataData(in3node, 0.0)

    in3node = addDataNode(in2node, 'ScilabDouble', height=1, width=3)
    addDataData(in3node, 2.0)
    addDataData(in3node, 1.0)
    addDataData(in3node, 1.0)

    innode = addDataNode(node, 'ScilabString', height=1, width=1)
    addDataData(innode, '')

    innode = addNode(node, 'Array', scilabClass='ScilabList')

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'integerParameters'}, height=0, width=0)

    node = addNode(outnode, 'Array', **{'as': 'objectsParameters'},
        scilabClass='ScilabList')

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'nbZerosCrossing'}, height=1, width=1)
    addDataData(node, 0.0)

    node = addDataNode(outnode, 'ScilabDouble', **{'as': 'nmode'}, height=1, width=1)
    addDataData(node, 0.0)

    node = addNode(outnode, 'Array', **{'as': 'oDState'},
        scilabClass='ScilabList')

    node = addNode(outnode, 'Array', **{'as': 'equations'},
        scilabClass='ScilabList')

    node = addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
        height='40.0', width='40.0', x='430.0', y='60.0')
