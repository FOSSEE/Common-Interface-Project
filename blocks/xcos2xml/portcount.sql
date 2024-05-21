.mode csv
SELECT block_name,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'ExplicitInputPort') AS explicitInputPorts,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'ImplicitInputPort') AS implicitInputPorts,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'ExplicitOutputPort') AS explicitOutputPorts,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'ImplicitOutputPort') AS implicitOutputPorts,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'ControlPort') AS controlPorts,
(SELECT COUNT(*) FROM xcosblocks_newblockport AS blockport WHERE blockport.block_id = block.id AND port_type = 'CommandPort') AS commandPorts,
0
FROM xcosblocks_newblock AS block
ORDER BY 1;
